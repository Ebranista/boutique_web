"""
Expense and Expense Category Models
"""
from decimal import Decimal
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class ExpenseCategory(BaseModel):
    """Expense category model"""
    __tablename__ = 'expense_categories'
    
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    is_recurring = db.Column(db.Boolean, default=False, nullable=False)
    
    # Relationships
    expenses = db.relationship('Expense', back_populates='category')
    
    def __repr__(self) -> str:
        return f"<ExpenseCategory {self.name}>"


class Expense(BaseModel):
    """Expense model"""
    __tablename__ = 'expenses'
    
    # Basic Information
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    
    # Category
    category_id = db.Column(
        db.String(36),
        db.ForeignKey('expense_categories.id'),
        nullable=False
    )
    
    # Financial
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Date
    expense_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Recurring
    is_recurring = db.Column(db.Boolean, default=False, nullable=False)
    recurring_month = db.Column(db.Integer)  # 1-12 for monthly recurring
    
    # Receipt
    receipt_image = db.Column(db.String(255))
    
    # Notes
    notes = db.Column(db.Text)
    
    # User
    created_by = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    # Relationships
    category = db.relationship('ExpenseCategory', back_populates='expenses')
    
    @property
    def month(self) -> int:
        """Get expense month"""
        return self.expense_date.month
    
    @property
    def year(self) -> int:
        """Get expense year"""
        return self.expense_date.year
    
    def __repr__(self) -> str:
        return f"<Expense {self.name} - {self.amount}>"
