"""
Sale Service
"""
from typing import Optional, List, Dict, Any
from decimal import Decimal
from datetime import datetime
import random
import string
from app.repositories.sale_repository import SaleRepository
from app.models.sale import Sale, SaleItem
from app.models.product import Product
from app.extensions import db


class SaleService:
    """Sale service with business logic"""
    
    def __init__(self):
        self.sale_repository = SaleRepository()
    
    def generate_invoice_number(self) -> str:
        """Generate unique invoice number"""
        while True:
            number = 'INV-' + datetime.now().strftime('%Y%m%d') + '-' + ''.join(
                random.choices(string.digits, k=6)
            )
            if not self.sale_repository.invoice_number_exists(number):
                return number
    
    def generate_receipt_number(self) -> str:
        """Generate unique receipt number"""
        while True:
            number = 'RCP-' + datetime.now().strftime('%Y%m%d') + '-' + ''.join(
                random.choices(string.digits, k=6)
            )
            if not self.sale_repository.receipt_number_exists(number):
                return number
    
    def create_sale(self, data: Dict[str, Any], cashier_id: str) -> Optional[Sale]:
        """
        Create a new sale
        
        Args:
            data: Sale data
            cashier_id: Cashier user ID
            
        Returns:
            Created sale or None if validation fails
        """
        # Validate customer if provided
        if data.get('customer_id'):
            from app.models.customer import Customer
            customer = Customer.query.filter_by(id=data['customer_id']).first()
            if not customer:
                raise ValueError('Customer not found')
        
        # Generate numbers
        invoice_number = self.generate_invoice_number()
        receipt_number = self.generate_receipt_number()
        
        # Create sale
        sale = Sale(
            invoice_number=invoice_number,
            receipt_number=receipt_number,
            customer_id=data.get('customer_id'),
            discount=Decimal(str(data.get('discount', 0))),
            payment_method=data['payment_method'],
            cash_received=Decimal(str(data.get('cash_received', 0))),
            notes=data.get('notes'),
            cashier_id=cashier_id
        )
        
        db.session.add(sale)
        db.session.flush()
        
        # Add items
        from app.services.inventory_service import InventoryService
        inventory_service = InventoryService()
        
        for item_data in data['items']:
            # Get product
            product = Product.query.filter_by(id=item_data['product_id']).first()
            if not product:
                raise ValueError(f'Product {item_data["product_id"]} not found')
            
            # Check stock
            if product.quantity < item_data['quantity']:
                raise ValueError(f'Insufficient stock for product {product.name}')
            
            item = SaleItem(
                sale_id=sale.id,
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                unit_price=Decimal(str(item_data['unit_price'])),
                discount=Decimal(str(item_data.get('discount', 0))),
                unit_cost=product.buying_price,
                subtotal=(Decimal(str(item_data['unit_price'])) * item_data['quantity']) - Decimal(str(item_data.get('discount', 0)))
            )
            db.session.add(item)
            
            # Stock out
            inventory_service.stock_out(
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                reference_type='sale',
                reference_id=sale.id,
                performed_by=cashier_id
            )
        
        # Calculate totals
        sale.calculate_totals()
        
        # Add loyalty points if customer
        if sale.customer_id:
            from app.services.customer_service import CustomerService
            customer_service = CustomerService()
            points = int(sale.total)  # 1 point per currency unit
            customer_service.add_loyalty_points(sale.customer_id, points)
        
        db.session.commit()
        db.session.refresh(sale)
        
        return sale
    
    def update_sale(self, sale_id: str, data: Dict[str, Any]) -> Optional[Sale]:
        """
        Update sale details
        
        Args:
            sale_id: Sale ID
            data: Sale data to update
            
        Returns:
            Updated sale or None
        """
        sale = self.sale_repository.get_by_id(sale_id)
        if not sale:
            return None

        if data.get('customer_id'):
            from app.models.customer import Customer
            customer = Customer.query.filter_by(id=data['customer_id']).first()
            if not customer:
                raise ValueError('Customer not found')
            sale.customer_id = data['customer_id']

        if 'payment_method' in data and data['payment_method'] is not None:
            sale.payment_method = data['payment_method']

        if 'discount' in data and data['discount'] is not None:
            sale.discount = Decimal(str(data['discount']))

        if 'cash_received' in data and data['cash_received'] is not None:
            sale.cash_received = Decimal(str(data['cash_received']))

        if 'notes' in data:
            sale.notes = data['notes']

        sale.calculate_totals()
        db.session.commit()
        db.session.refresh(sale)
        return sale

    def refund_sale(self, sale_id: str) -> Optional[Sale]:
        """
        Refund a sale
        
        Args:
            sale_id: Sale ID
            
        Returns:
            Updated sale or None
        """
        sale = self.sale_repository.get_by_id(sale_id)
        if not sale:
            return None
        
        if sale.status == 'refunded':
            raise ValueError('Sale already refunded')
        
        # Reverse stock
        from app.services.inventory_service import InventoryService
        inventory_service = InventoryService()
        
        for item in sale.items:
            inventory_service.stock_in(
                product_id=item.product_id,
                quantity=item.quantity,
                buying_price=item.unit_cost,
                reference_type='refund',
                reference_id=sale.id,
                performed_by=sale.cashier_id
            )
        
        sale.status = 'refunded'
        db.session.commit()
        db.session.refresh(sale)
        
        return sale
    
    def cancel_sale(self, sale_id: str) -> Optional[Sale]:
        """
        Cancel a sale
        
        Args:
            sale_id: Sale ID
            
        Returns:
            Updated sale or None
        """
        sale = self.sale_repository.get_by_id(sale_id)
        if not sale:
            return None
        
        # Reverse stock
        from app.services.inventory_service import InventoryService
        inventory_service = InventoryService()
        
        for item in sale.items:
            inventory_service.stock_in(
                product_id=item.product_id,
                quantity=item.quantity,
                buying_price=item.unit_cost,
                reference_type='sale_cancellation',
                reference_id=sale.id,
                performed_by=sale.cashier_id
            )
        
        sale.status = 'cancelled'
        db.session.commit()
        db.session.refresh(sale)
        
        return sale
    
    def delete_sale(self, sale_id: str) -> bool:
        """Soft delete a sale"""
        return self.sale_repository.delete(sale_id)

    def get_sale_by_id(self, sale_id: str) -> Optional[Sale]:
        """Get sale by ID"""
        return self.sale_repository.get_by_id(sale_id)
    
    def get_all_sales(self, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get all sales"""
        return self.sale_repository.get_all(page, per_page)
    
    def get_today_sales(self, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get today's sales"""
        return self.sale_repository.get_today_sales(page, per_page)
    
    def get_by_customer(self, customer_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get sales by customer"""
        return self.sale_repository.get_by_customer(customer_id, page, per_page)
