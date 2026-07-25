"""
Inventory and Stock Movement Models
"""
from decimal import Decimal
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class Inventory(BaseModel):
    """Inventory model tracking product stock"""
    __tablename__ = 'inventory'
    
    product_id = db.Column(
        db.String(36),
        db.ForeignKey('products.id'),
        unique=True,
        nullable=False
    )
    quantity = db.Column(db.Integer, default=0, nullable=False)
    reserved_quantity = db.Column(db.Integer, default=0, nullable=False)
    available_quantity = db.Column(db.Integer, default=0, nullable=False)
    
    # Valuation
    average_cost = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    total_value = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Relationships
    product = db.relationship('Product', back_populates='inventory')
    stock_movements = db.relationship('StockMovement', back_populates='inventory')
    
    @property
    def is_low_stock(self) -> bool:
        """Check if inventory is low on stock"""
        if self.product:
            return self.quantity <= self.product.minimum_stock
        return False
    
    @property
    def is_out_of_stock(self) -> bool:
        """Check if inventory is out of stock"""
        return self.quantity == 0
    
    def update_available_quantity(self) -> None:
        """Update available quantity"""
        self.available_quantity = self.quantity - self.reserved_quantity
    
    def __repr__(self) -> str:
        return f"<Inventory Product: {self.product_id} Qty: {self.quantity}>"


class StockMovement(BaseModel):
    """Stock movement model for tracking inventory changes"""
    __tablename__ = 'stock_movements'
    
    inventory_id = db.Column(
        db.String(36),
        db.ForeignKey('inventory.id'),
        nullable=False
    )
    product_id = db.Column(
        db.String(36),
        db.ForeignKey('products.id'),
        nullable=False
    )
    
    # Movement Details
    movement_type = db.Column(
        db.String(20),
        nullable=False
    )  # stock_in, stock_out, adjustment, transfer
    quantity = db.Column(db.Integer, nullable=False)
    previous_quantity = db.Column(db.Integer, nullable=False)
    new_quantity = db.Column(db.Integer, nullable=False)
    
    # Reference
    reference_type = db.Column(db.String(50))  # purchase, sale, adjustment, etc.
    reference_id = db.Column(db.String(36))
    
    # Notes
    reason = db.Column(db.String(255))
    notes = db.Column(db.Text)
    
    # User
    performed_by = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    # Relationships
    inventory = db.relationship('Inventory', back_populates='stock_movements')
    product = db.relationship('Product', back_populates='stock_movements')
    
    def __repr__(self) -> str:
        return f"<StockMovement {self.movement_type} Qty: {self.quantity}>"
