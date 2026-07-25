"""
Supplier Model
"""
from decimal import Decimal
from app.extensions import db
from .base import BaseModel


class Supplier(BaseModel):
    """Supplier model"""
    __tablename__ = 'suppliers'
    
    # Basic Information
    name = db.Column(db.String(100), nullable=False, index=True)
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    address = db.Column(db.String(255))
    
    # Business Information
    tin_number = db.Column(db.String(50))
    
    # Financial
    outstanding_balance = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Status
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Relationships
    products = db.relationship('Product', back_populates='supplier')
    purchases = db.relationship('Purchase', back_populates='supplier')
    
    @property
    def total_purchases(self) -> int:
        """Get total number of purchases"""
        return len([p for p in self.purchases if not p.is_deleted])
    
    @property
    def total_products_supplied(self) -> int:
        """Get total number of unique products supplied"""
        return len(self.products)
    
    def __repr__(self) -> str:
        return f"<Supplier {self.name}>"
