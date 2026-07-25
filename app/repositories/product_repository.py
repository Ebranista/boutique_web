"""
Product Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.product import Product


class ProductRepository(BaseRepository[Product]):
    """Product repository with specific operations"""
    
    def __init__(self):
        super().__init__(Product)
    
    def get_by_product_code(self, product_code: str) -> Optional[Product]:
        """Get product by product code"""
        return self.model.query.filter_by(product_code=product_code).first()
    
    def get_by_barcode(self, barcode: str) -> Optional[Product]:
        """Get product by barcode"""
        return self.model.query.filter_by(barcode=barcode).first()
    
    def get_by_category(self, category_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get products by category"""
        query = self.model.query.filter_by(
            category_id=category_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_brand(self, brand_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get products by brand"""
        query = self.model.query.filter_by(
            brand_id=brand_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_supplier(self, supplier_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get products by supplier"""
        query = self.model.query.filter_by(
            supplier_id=supplier_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_gender(self, gender: str, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get products by gender"""
        query = self.model.query.filter_by(
            gender=gender,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_low_stock(self, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get low stock products"""
        from app.models.product import Product
        query = self.model.query.filter(
            self.model.quantity <= self.model.minimum_stock,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_out_of_stock(self, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Get out of stock products"""
        query = self.model.query.filter_by(
            quantity=0,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def search_products(self, search_term: str, page: int = 1, per_page: int = 20) -> tuple[List[Product], int]:
        """Search products by name or code"""
        query = self.model.query.filter(
            (self.model.name.ilike(f'%{search_term}%')) |
            (self.model.product_code.ilike(f'%{search_term}%')) |
            (self.model.barcode.ilike(f'%{search_term}%')),
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def product_code_exists(self, product_code: str, exclude_id: str = None) -> bool:
        """Check if product code exists"""
        query = self.model.query.filter_by(product_code=product_code)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def barcode_exists(self, barcode: str, exclude_id: str = None) -> bool:
        """Check if barcode exists"""
        query = self.model.query.filter_by(barcode=barcode)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
