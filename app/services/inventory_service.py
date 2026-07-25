"""
Inventory Service
"""
from typing import Optional, List, Dict, Any
from decimal import Decimal
from app.repositories.inventory_repository import InventoryRepository
from app.models.inventory import Inventory, StockMovement
from app.models.product import Product
from app.extensions import db


class InventoryService:
    """Inventory service with business logic"""
    
    def __init__(self):
        self.inventory_repository = InventoryRepository()
    
    def _sync_product_quantity(self, inventory: Inventory) -> None:
        """Keep the product quantity field in sync with inventory."""
        if inventory and inventory.product:
            inventory.product.quantity = inventory.quantity
            db.session.add(inventory.product)
    
    def create_inventory(self, product_id: str, quantity: int = 0) -> Optional[Inventory]:
        """
        Create inventory record for product
        
        Args:
            product_id: Product ID
            quantity: Initial quantity
            
        Returns:
            Created inventory or None
        """
        if self.inventory_repository.get_by_product(product_id):
            raise ValueError('Inventory already exists for this product')
        
        inventory = self.inventory_repository.create(
            product_id=product_id,
            quantity=quantity,
            reserved_quantity=0,
            available_quantity=quantity,
            average_cost=Decimal('0.00'),
            total_value=Decimal('0.00')
        )
        self._sync_product_quantity(inventory)
        return inventory
    
    def stock_in(
        self,
        product_id: str,
        quantity: int,
        buying_price: Decimal,
        reference_type: str = None,
        reference_id: str = None,
        performed_by: str = None,
        notes: str = None
    ) -> Optional[Inventory]:
        """
        Add stock to inventory
        
        Args:
            product_id: Product ID
            quantity: Quantity to add
            buying_price: Buying price
            reference_type: Reference type (purchase, adjustment, etc.)
            reference_id: Reference ID
            performed_by: User ID
            notes: Notes
            
        Returns:
            Updated inventory or None
        """
        inventory = self.inventory_repository.get_by_product(product_id)
        if not inventory:
            inventory = self.create_inventory(product_id, 0)
        
        if not inventory:
            return None
        
        previous_quantity = inventory.quantity
        new_quantity = previous_quantity + quantity
        
        # Update average cost
        if inventory.quantity > 0:
            total_cost = (inventory.average_cost * inventory.quantity) + (buying_price * quantity)
            inventory.average_cost = total_cost / new_quantity
        else:
            inventory.average_cost = buying_price
        
        # Update inventory
        inventory.quantity = new_quantity
        inventory.total_value = inventory.average_cost * new_quantity
        inventory.update_available_quantity()
        self._sync_product_quantity(inventory)
        
        # Create stock movement
        stock_movement = StockMovement(
            inventory_id=inventory.id,
            product_id=product_id,
            movement_type='stock_in',
            quantity=quantity,
            previous_quantity=previous_quantity,
            new_quantity=new_quantity,
            reference_type=reference_type,
            reference_id=reference_id,
            reason='Stock in',
            notes=notes,
            performed_by=performed_by
        )
        
        db.session.add(stock_movement)
        db.session.commit()
        db.session.refresh(inventory)
        
        return inventory
    
    def stock_out(
        self,
        product_id: str,
        quantity: int,
        reference_type: str = None,
        reference_id: str = None,
        performed_by: str = None,
        notes: str = None
    ) -> Optional[Inventory]:
        """
        Remove stock from inventory
        
        Args:
            product_id: Product ID
            quantity: Quantum to remove
            reference_type: Reference type (sale, adjustment, etc.)
            reference_id: Reference ID
            performed_by: User ID
            notes: Notes
            
        Returns:
            Updated inventory or None
        """
        inventory = self.inventory_repository.get_by_product(product_id)
        if not inventory:
            raise ValueError('Inventory not found for this product')
        
        if inventory.quantity < quantity:
            raise ValueError('Insufficient stock')
        
        previous_quantity = inventory.quantity
        new_quantity = previous_quantity - quantity
        
        # Update inventory
        inventory.quantity = new_quantity
        inventory.total_value = inventory.average_cost * new_quantity
        inventory.update_available_quantity()
        self._sync_product_quantity(inventory)
        
        # Create stock movement
        stock_movement = StockMovement(
            inventory_id=inventory.id,
            product_id=product_id,
            movement_type='stock_out',
            quantity=quantity,
            previous_quantity=previous_quantity,
            new_quantity=new_quantity,
            reference_type=reference_type,
            reference_id=reference_id,
            reason='Stock out',
            notes=notes,
            performed_by=performed_by
        )
        
        db.session.add(stock_movement)
        db.session.commit()
        db.session.refresh(inventory)
        
        return inventory
    
    def adjust_stock(
        self,
        product_id: str,
        quantity: int,
        adjustment_type: str,
        reason: str,
        performed_by: str,
        notes: str = None
    ) -> Optional[Inventory]:
        """
        Adjust stock (add, subtract, or set)
        
        Args:
            product_id: Product ID
            quantity: Quantity
            adjustment_type: Type (add, subtract, set)
            reason: Reason for adjustment
            performed_by: User ID
            notes: Notes
            
        Returns:
            Updated inventory or None
        """
        inventory = self.inventory_repository.get_by_product(product_id)
        if not inventory:
            raise ValueError('Inventory not found for this product')
        
        previous_quantity = inventory.quantity
        
        if adjustment_type == 'add':
            new_quantity = previous_quantity + quantity
        elif adjustment_type == 'subtract':
            if previous_quantity < quantity:
                raise ValueError('Cannot subtract more than current quantity')
            new_quantity = previous_quantity - quantity
        elif adjustment_type == 'set':
            new_quantity = quantity
        else:
            raise ValueError('Invalid adjustment type')
        
        if new_quantity < 0:
            raise ValueError('Quantity cannot be negative')
        
        # Update inventory
        inventory.quantity = new_quantity
        inventory.total_value = inventory.average_cost * new_quantity
        inventory.update_available_quantity()
        self._sync_product_quantity(inventory)
        
        # Create stock movement
        stock_movement = StockMovement(
            inventory_id=inventory.id,
            product_id=product_id,
            movement_type='adjustment',
            quantity=quantity,
            previous_quantity=previous_quantity,
            new_quantity=new_quantity,
            reference_type='adjustment',
            reason=reason,
            notes=notes,
            performed_by=performed_by
        )
        
        db.session.add(stock_movement)
        db.session.commit()
        db.session.refresh(inventory)
        
        return inventory
    
    def get_inventory_by_product(self, product_id: str) -> Optional[Inventory]:
        """Get inventory by product ID"""
        return self.inventory_repository.get_by_product(product_id)
    
    def get_low_stock(self, page: int = 1, per_page: int = 20) -> tuple[List[Inventory], int]:
        """Get low stock inventory"""
        return self.inventory_repository.get_low_stock(page, per_page)
    
    def get_out_of_stock(self, page: int = 1, per_page: int = 20) -> tuple[List[Inventory], int]:
        """Get out of stock inventory"""
        return self.inventory_repository.get_out_of_stock(page, per_page)

    def get_stock_movements(
        self,
        product_id: str = None,
        inventory_id: str = None,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[StockMovement], int]:
        """Get stock movement history"""
        return self.inventory_repository.get_stock_movements(
            product_id=product_id,
            inventory_id=inventory_id,
            page=page,
            per_page=per_page
        )
