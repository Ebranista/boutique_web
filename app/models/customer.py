"""
Customer Model
"""
from datetime import date
from decimal import Decimal
from app.extensions import db
from .base import BaseModel


class Customer(BaseModel):
    """Customer model"""
    __tablename__ = 'customers'
    
    # Basic Information
    name = db.Column(db.String(100), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    address = db.Column(db.String(255))
    
    # Personal Information
    gender = db.Column(db.String(10))  # male, female, other
    birthday = db.Column(db.Date)
    
    # Media
    image = db.Column(db.String(255))
    
    # Loyalty
    loyalty_points = db.Column(db.Integer, default=0, nullable=False)
    
    # Status
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Relationships
    sales = db.relationship('Sale', back_populates='customer')
    
    @property
    def total_purchases(self) -> int:
        """Get total number of purchases"""
        return len([s for s in self.sales if not s.is_deleted])
    
    @property
    def total_spent(self) -> Decimal:
        """Calculate total amount spent"""
        total = Decimal('0.00')
        for sale in self.sales:
            if not sale.is_deleted:
                total += sale.total
        return total
    
    @property
    def age(self) -> int:
        """Calculate customer age"""
        if self.birthday:
            today = date.today()
            return today.year - self.birthday.year - (
                (today.month, today.day) < (self.birthday.month, self.birthday.day)
            )
        return 0
    
    def __repr__(self) -> str:
        return f"<Customer {self.name}>"
