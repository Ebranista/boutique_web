"""
Inventory Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.inventory import Inventory, StockMovement
from app.extensions import db


class InventoryRepository(BaseRepository[Inventory]):
    """Inventory repository with specific operations"""
    
    def __init__(self):
        super().__init__(Inventory)
    
    def get_by_product(self, product_id: str) -> Optional[Inventory]:
        """Get inventory by product ID"""
        return self.model.query.filter_by(product_id=product_id).first()
    
    def get_low_stock(self, page: int = 1, per_page: int = 20) -> tuple[List[Inventory], int]:
        """Get low stock inventory"""
        from app.models.product import Product
        query = self.model.query.join(Product).filter(
            self.model.quantity <= Product.minimum_stock,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_out_of_stock(self, page: int = 1, per_page: int = 20) -> tuple[List[Inventory], int]:
        """Get out of stock inventory"""
        query = self.model.query.filter_by(
            quantity=0,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total

    def get_stock_movements(
        self,
        product_id: str = None,
        inventory_id: str = None,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[StockMovement], int]:
        """Get stock movement history"""
        query = StockMovement.query.filter(StockMovement.is_deleted == False)
        if product_id:
            query = query.filter_by(product_id=product_id)
        if inventory_id:
            query = query.filter_by(inventory_id=inventory_id)
        pagination = query.order_by(StockMovement.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def update_quantity(self, product_id: str, quantity: int) -> Optional[Inventory]:
        """Update inventory quantity"""
        inventory = self.get_by_product(product_id)
        if inventory:
            inventory.quantity = quantity
            inventory.update_available_quantity()
            db.session.commit()
            db.session.refresh(inventory)
        return inventory
    
    def adjust_quantity(self, product_id: str, adjustment: int) -> Optional[Inventory]:
        """Adjust inventory quantity by adding/subtracting"""
        inventory = self.get_by_product(product_id)
        if inventory:
            new_quantity = inventory.quantity + adjustment
            if new_quantity >= 0:
                inventory.quantity = new_quantity
                inventory.update_available_quantity()
                db.session.commit()
                db.session.refresh(inventory)
        return inventory
