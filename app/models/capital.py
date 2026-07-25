"""
Capital Model
"""
from decimal import Decimal
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class Capital(BaseModel):
    """Capital model for tracking business capital"""
    __tablename__ = 'capital'
    
    # Financial
    beginning_capital = db.Column(db.Numeric(12, 2), default=Decimal('0.00'))
    current_capital = db.Column(db.Numeric(12, 2), default=Decimal('0.00'))
    total_invested = db.Column(db.Numeric(12, 2), default=Decimal('0.00'))
    total_withdrawn = db.Column(db.Numeric(12, 2), default=Decimal('0.00'))
    
    # Period
    period_start = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    period_end = db.Column(db.DateTime, nullable=True)
    
    # Status
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    @property
    def capital_growth(self) -> Decimal:
        """Calculate capital growth"""
        if self.beginning_capital == 0:
            return Decimal('0.00')
        return ((self.current_capital - self.beginning_capital) / self.beginning_capital) * 100
    
    def __repr__(self) -> str:
        return f"<Capital Current: {self.current_capital}>"
