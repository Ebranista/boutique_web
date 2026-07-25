"""
Purchase and Purchase Item Models
"""
from decimal import Decimal
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class Purchase(BaseModel):
    """Purchase model for buying from suppliers"""
    __tablename__ = 'purchases'
    
    # Identification
    purchase_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    
    # Supplier
    supplier_id = db.Column(
        db.String(36),
        db.ForeignKey('suppliers.id'),
        nullable=False
    )
    
    # Financial
    subtotal = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    discount = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    tax = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    total = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Payment
    payment_method = db.Column(
        db.String(50),
        nullable=False
    )  # cash, bank_transfer, credit
    paid_amount = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    balance = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Dates
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Status
    status = db.Column(
        db.String(20),
        default='pending',
        nullable=False
    )  # pending, completed, cancelled
    
    # Notes
    notes = db.Column(db.Text)
    receipt_image = db.Column(db.String(255))
    
    # User
    created_by = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    # Relationships
    supplier = db.relationship('Supplier', back_populates='purchases')
    items = db.relationship('PurchaseItem', back_populates='purchase', cascade='all, delete-orphan')
    
    @property
    def total_items(self) -> int:
        """Get total number of items"""
        return len(self.items)
    
    @property
    def total_quantity(self) -> int:
        """Get total quantity of all items"""
        return sum(item.quantity for item in self.items)
    
    def calculate_totals(self) -> None:
        """Calculate subtotal, tax, and total"""
        self.subtotal = sum(item.total for item in self.items)
        self.tax = self.subtotal * Decimal('0.18')  # 18% tax
        self.total = self.subtotal - self.discount + self.tax
        self.balance = self.total - self.paid_amount
    
    def __repr__(self) -> str:
        return f"<Purchase {self.purchase_number}>"


class PurchaseItem(BaseModel):
    """Purchase item model"""
    __tablename__ = 'purchase_items'
    
    purchase_id = db.Column(
        db.String(36),
        db.ForeignKey('purchases.id'),
        nullable=False
    )
    product_id = db.Column(
        db.String(36),
        db.ForeignKey('products.id'),
        nullable=False
    )
    
    # Details
    quantity = db.Column(db.Integer, nullable=False)
    buying_price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    subtotal = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Relationships
    purchase = db.relationship('Purchase', back_populates='items')
    product = db.relationship('Product', back_populates='purchase_items')
    
    @property
    def total(self) -> Decimal:
        """Calculate total for this item"""
        return (self.buying_price * self.quantity) - self.discount
    
    def __repr__(self) -> str:
        return f"<PurchaseItem Product: {self.product_id} Qty: {self.quantity}>"
