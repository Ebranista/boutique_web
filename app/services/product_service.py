"""
Product Service
"""
from typing import Optional, List, Dict, Any
from decimal import Decimal
import barcode
import qrcode
import io
import base64
from app.repositories.product_repository import ProductRepository
from app.models.product import Product
from app.extensions import db


class ProductService:
    """Product service with business logic"""
    
    def __init__(self):
        self.product_repository = ProductRepository()
    
    def generate_product_code(self) -> str:
        """Generate unique product code"""
        import random
        import string
        while True:
            code = 'PRD-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if not self.product_repository.product_code_exists(code):
                return code
    
    def generate_barcode(self, product_code: str) -> str:
        """
        Generate barcode for product
        
        Args:
            product_code: Product code
            
        Returns:
            Base64 encoded barcode image
        """
        barcode_class = barcode.get_barcode_class('code128')
        barcode_instance = barcode_class(product_code, writer=barcode.writer.ImageWriter())
        
        buffer = io.BytesIO()
        barcode_instance.write(buffer)
        barcode_image = base64.b64encode(buffer.getvalue()).decode()
        
        return barcode_image
    
    def generate_qr_code(self, product_id: str) -> str:
        """
        Generate QR code for product
        
        Args:
            product_id: Product ID
            
        Returns:
            Base64 encoded QR code image
        """
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(product_id)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer)
        qr_image = base64.b64encode(buffer.getvalue()).decode()
        
        return qr_image
    
    def create_product(self, data: Dict[str, Any], created_by: str) -> Optional[Product]:
        """
        Create a new product
        
        Args:
            data: Product data
            created_by: User ID who created the product
            
        Returns:
            Created product or None if validation fails
        """
        # Validate buying price vs selling price
        buying_price = Decimal(str(data['buying_price']))
        selling_price = Decimal(str(data['selling_price']))
        
        if buying_price > selling_price:
            raise ValueError('Buying price cannot exceed selling price')
        
        # Generate product code
        product_code = self.generate_product_code()
        
        # Use the product code as the barcode text (to fit database VARCHAR(50) and allow scanning/searching)
        barcode_str = product_code
        
        # Create product
        product = Product(
            product_code=product_code,
            barcode=barcode_str,
            name=data['name'],
            description=data.get('description'),
            category_id=data['category_id'],
            brand_id=data['brand_id'],
            gender=data['gender'],
            color=data.get('color'),
            size=data.get('size'),
            buying_price=buying_price,
            selling_price=selling_price,
            minimum_stock=data.get('minimum_stock', 10),
            supplier_id=data.get('supplier_id'),
            image=data.get('image'),
            created_by=created_by
        )
        
        db.session.add(product)
        db.session.commit()
        db.session.refresh(product)
        
        # Create inventory record
        from app.services.inventory_service import InventoryService
        inventory_service = InventoryService()
        inventory_service.create_inventory(product.id, 0)
        
        return product
    
    def update_product(self, product_id: str, data: Dict[str, Any]) -> Optional[Product]:
        """
        Update product
        
        Args:
            product_id: Product ID
            data: Product data to update
            
        Returns:
            Updated product or None
        """
        product = self.product_repository.get_by_id(product_id)
        if not product:
            return None
        
        # Validate buying price vs selling price
        if 'buying_price' in data and 'selling_price' in data:
            buying_price = Decimal(str(data['buying_price']))
            selling_price = Decimal(str(data['selling_price']))
            
            if buying_price > selling_price:
                raise ValueError('Buying price cannot exceed selling price')
        
        # Update fields
        for key, value in data.items():
            if hasattr(product, key) and key not in ['product_code', 'barcode', 'created_by']:
                setattr(product, key, value)
        
        db.session.commit()
        db.session.refresh(product)
        
        return product
    
    def delete_product(self, product_id: str) -> bool:
        """
        Delete product (soft delete)
        
        Args:
            product_id: Product ID
            
        Returns:
            True if deleted
        """
        return self.product_repository.delete(product_id)
    
    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Get product by ID"""
        return self.product_repository.get_by_id(product_id)
    
    def get_product_by_barcode(self, barcode: str) -> Optional[Product]:
        """Get product by barcode"""
        return self.product_repository.get_by_barcode(barcode)
    
    def get_all_products(
        self,
        page: int = 1,
        per_page: int = 20,
        filters: Dict[str, Any] = None
    ) -> tuple[List[Product], int]:
        """Get all products"""
        return self.product_repository.get_all(page, per_page, filters)
    
    def search_products(self, search_term: str, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Search products"""
        return self.product_repository.search_products(search_term, page, per_page)
    
    def get_low_stock_products(self, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get low stock products"""
        return self.product_repository.get_low_stock(page, per_page)
    
    def get_out_of_stock_products(self, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get out of stock products"""
        return self.product_repository.get_out_of_stock(page, per_page)
