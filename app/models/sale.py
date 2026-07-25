"""
Sale and Sale Item Models
"""
from decimal import Decimal
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class Sale(BaseModel):
    """Sale model for POS transactions"""
    __tablename__ = 'sales'
    
    # Identification
    invoice_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    receipt_number = db.Column(db.String(20), unique=True, nullable=False)
    
    # Customer
    customer_id = db.Column(
        db.String(36),
        db.ForeignKey('customers.id'),
        nullable=True
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
    )  # cash, card, mobile_money, bank_transfer
    cash_received = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    change = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Profit
    total_cost = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    total_profit = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Status
    status = db.Column(
        db.String(20),
        default='completed',
        nullable=False
    )  # pending, completed, cancelled, refunded
    
    # Dates
    sale_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Notes
    notes = db.Column(db.Text)
    
    # User
    cashier_id = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    # Relationships
    customer = db.relationship('Customer', back_populates='sales')
    cashier = db.relationship('User', back_populates='sales')
    items = db.relationship('SaleItem', back_populates='sale', cascade='all, delete-orphan')
    
    @property
    def total_items(self) -> int:
        """Get total number of items"""
        return len(self.items)
    
    @property
    def total_quantity(self) -> int:
        """Get total quantity of all items"""
        return sum(item.quantity for item in self.items)
    
    def calculate_totals(self) -> None:
        """Calculate subtotal, tax, total, cost, and profit"""
        self.subtotal = sum(item.total for item in self.items)
        self.total_cost = sum(item.total_cost for item in self.items)
        self.tax = self.subtotal * Decimal('0.18')  # 18% tax
        self.total = self.subtotal - self.discount + self.tax
        self.total_profit = self.total - self.total_cost
        self.change = self.cash_received - self.total
    
    def __repr__(self) -> str:
        return f"<Sale {self.invoice_number}>"


class SaleItem(BaseModel):
    """Sale item model"""
    __tablename__ = 'sale_items'
    
    sale_id = db.Column(
        db.String(36),
        db.ForeignKey('sales.id'),
        nullable=False
    )
    product_id = db.Column(
        db.String(36),
        db.ForeignKey('products.id'),
        nullable=False
    )
    
    # Details
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    subtotal = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
    
    # Cost
    unit_cost = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Relationships
    sale = db.relationship('Sale', back_populates='items')
    product = db.relationship('Product', back_populates='sale_items')
    
    @property
    def total(self) -> Decimal:
        """Calculate total for this item"""
        return (self.unit_price * self.quantity) - self.discount
    
    @property
    def total_cost(self) -> Decimal:
        """Calculate total cost for this item"""
        return self.unit_cost * self.quantity
    
    @property
    def total_profit(self) -> Decimal:
        """Calculate profit for this item"""
        return self.total - self.total_cost
    
    def __repr__(self) -> str:
        return f"<SaleItem Product: {self.product_id} Qty: {self.quantity}>"
