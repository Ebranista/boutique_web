"""
Setting Model
"""
from app.extensions import db
from .base import BaseModel


class Setting(BaseModel):
    """Setting model for application configuration"""
    __tablename__ = 'settings'
    
    # Basic Information
    shop_name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    
    # Currency
    currency = db.Column(db.String(3), default='USD', nullable=False)
    currency_symbol = db.Column(db.String(5), default='$', nullable=False)
    
    # Tax
    tax_percentage = db.Column(db.Integer, default=18, nullable=False)
    
    # Receipt
    receipt_footer = db.Column(db.Text)
    receipt_header = db.Column(db.Text)
    
    # Inventory
    low_stock_limit = db.Column(db.Integer, default=10, nullable=False)
    
    # UI
    dark_mode = db.Column(db.Boolean, default=False, nullable=False)
    
    # Business
    tin_number = db.Column(db.String(50))
    
    def __repr__(self) -> str:
        return f"<Setting {self.shop_name}>"
