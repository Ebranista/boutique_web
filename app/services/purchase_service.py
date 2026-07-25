"""
Purchase Service
"""
from typing import Optional, List, Dict, Any
from decimal import Decimal
from datetime import datetime
import random
import string
from app.repositories.purchase_repository import PurchaseRepository
from app.models.purchase import Purchase, PurchaseItem
from app.models.supplier import Supplier
from app.extensions import db


class PurchaseService:
    """Purchase service with business logic"""
    
    def __init__(self):
        self.purchase_repository = PurchaseRepository()
    
    def generate_purchase_number(self) -> str:
        """Generate unique purchase number"""
        while True:
            number = 'PUR-' + datetime.now().strftime('%Y%m%d') + '-' + ''.join(
                random.choices(string.digits, k=4)
            )
            if not self.purchase_repository.purchase_number_exists(number):
                return number
    
    def create_purchase(self, data: Dict[str, Any], created_by: str) -> Optional[Purchase]:
        """
        Create a new purchase
        
        Args:
            data: Purchase data
            created_by: User ID who created the purchase
            
        Returns:
            Created purchase or None if validation fails
        """
        # Validate supplier
        supplier = Supplier.query.filter_by(id=data['supplier_id']).first()
        if not supplier:
            raise ValueError('Supplier not found')
        
        # Generate purchase number
        purchase_number = self.generate_purchase_number()
        
        # Create purchase
        purchase = Purchase(
            purchase_number=purchase_number,
            supplier_id=data['supplier_id'],
            discount=Decimal(str(data.get('discount', 0))),
            payment_method=data['payment_method'],
            paid_amount=Decimal(str(data.get('paid_amount', 0))),
            notes=data.get('notes'),
            receipt_image=data.get('receipt_image'),
            created_by=created_by
        )
        
        db.session.add(purchase)
        db.session.flush()
        
        # Add items
        from app.services.inventory_service import InventoryService
        inventory_service = InventoryService()
        
        for item_data in data['items']:
            item = PurchaseItem(
                purchase_id=purchase.id,
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                buying_price=Decimal(str(item_data['buying_price'])),
                discount=Decimal(str(item_data.get('discount', 0))),
                subtotal=(Decimal(str(item_data['buying_price'])) * item_data['quantity']) - Decimal(str(item_data.get('discount', 0)))
            )
            db.session.add(item)
            
            # Stock in
            inventory_service.stock_in(
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                buying_price=Decimal(str(item_data['buying_price'])),
                reference_type='purchase',
                reference_id=purchase.id,
                performed_by=created_by
            )
        
        # Calculate totals
        purchase.calculate_totals()
        
        # Update supplier balance
        if purchase.balance > 0:
            supplier.outstanding_balance += purchase.balance
        
        db.session.commit()
        db.session.refresh(purchase)
        
        return purchase
    
    def complete_purchase(self, purchase_id: str) -> Optional[Purchase]:
        """
        Complete a purchase
        
        Args:
            purchase_id: Purchase ID
            
        Returns:
            Updated purchase or None
        """
        purchase = self.purchase_repository.get_by_id(purchase_id)
        if not purchase:
            return None
        
        purchase.status = 'completed'
        db.session.commit()
        db.session.refresh(purchase)
        
        return purchase
    
    def cancel_purchase(self, purchase_id: str) -> Optional[Purchase]:
        """
        Cancel a purchase
        
        Args:
            purchase_id: Purchase ID
            
        Returns:
            Updated purchase or None
        """
        purchase = self.purchase_repository.get_by_id(purchase_id)
        if not purchase:
            return None
        
        # Reverse stock
        from app.services.inventory_service import InventoryService
        inventory_service = InventoryService()
        
        for item in purchase.items:
            inventory_service.stock_out(
                product_id=item.product_id,
                quantity=item.quantity,
                reference_type='purchase_cancellation',
                reference_id=purchase.id,
                performed_by=purchase.created_by
            )
        
        purchase.status = 'cancelled'
        db.session.commit()
        db.session.refresh(purchase)
        
        return purchase
    
    def update_purchase(self, purchase_id: str, data: Dict[str, Any]) -> Optional[Purchase]:
        """Update purchase details"""
        purchase = self.purchase_repository.get_by_id(purchase_id)
        if not purchase:
            return None

        if 'supplier_id' in data and data.get('supplier_id'):
            supplier = Supplier.query.filter_by(id=data['supplier_id']).first()
            if not supplier:
                raise ValueError('Supplier not found')
            purchase.supplier_id = data['supplier_id']

        if 'discount' in data and data['discount'] is not None:
            purchase.discount = Decimal(str(data['discount']))

        if 'payment_method' in data and data['payment_method'] is not None:
            purchase.payment_method = data['payment_method']

        if 'paid_amount' in data and data['paid_amount'] is not None:
            purchase.paid_amount = Decimal(str(data['paid_amount']))

        if 'notes' in data:
            purchase.notes = data['notes']

        if 'receipt_image' in data:
            purchase.receipt_image = data['receipt_image']

        purchase.calculate_totals()
        db.session.commit()
        db.session.refresh(purchase)
        return purchase

    def delete_purchase(self, purchase_id: str) -> bool:
        """Soft delete a purchase"""
        return self.purchase_repository.delete(purchase_id)

    def get_purchase_by_id(self, purchase_id: str) -> Optional[Purchase]:
        """Get purchase by ID"""
        return self.purchase_repository.get_by_id(purchase_id)
    
    def get_all_purchases(self, page: int = 1, per_page: int = 20) -> tuple[List[Purchase], int]:
        """Get all purchases"""
        return self.purchase_repository.get_all(page, per_page)
    
    def get_by_supplier(self, supplier_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Purchase], int]:
        """Get purchases by supplier"""
        return self.purchase_repository.get_by_supplier(supplier_id, page, per_page)
