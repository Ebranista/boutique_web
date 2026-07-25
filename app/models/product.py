"""
Product, Category, and Brand Models
"""
from app.extensions import db
from .base import BaseModel


class Category(BaseModel):
    """Category model for products"""
    __tablename__ = 'categories'
    
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    
    # Relationships
    products = db.relationship('Product', back_populates='category')
    
    def __repr__(self) -> str:
        return f"<Category {self.name}>"


class Brand(BaseModel):
    """Brand model for products"""
    __tablename__ = 'brands'
    
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    
    # Relationships
    products = db.relationship('Product', back_populates='brand')
    
    def __repr__(self) -> str:
        return f"<Brand {self.name}>"


class Product(BaseModel):
    """Product model"""
    __tablename__ = 'products'
    
    # Identification
    product_code = db.Column(db.String(20), unique=True, nullable=False, index=True)
    barcode = db.Column(db.String(50), unique=True, index=True)
    qr_code = db.Column(db.String(255), unique=True)
    
    # Basic Information
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    
    # Classification
    category_id = db.Column(
        db.String(36),
        db.ForeignKey('categories.id'),
        nullable=False
    )
    brand_id = db.Column(
        db.String(36),
        db.ForeignKey('brands.id'),
        nullable=False
    )
    gender = db.Column(
        db.String(10),
        nullable=False,
        default='unisex'
    )  # men, women, kids, unisex
    
    # Attributes
    color = db.Column(db.String(50))
    size = db.Column(db.String(20))
    
    # Pricing
    buying_price = db.Column(db.Numeric(10, 2), nullable=False)
    selling_price = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Inventory
    quantity = db.Column(db.Integer, default=0, nullable=False)
    minimum_stock = db.Column(db.Integer, default=10, nullable=False)
    
    # Supplier
    supplier_id = db.Column(
        db.String(36),
        db.ForeignKey('suppliers.id'),
        nullable=True
    )
    
    # Media
    image = db.Column(db.String(255))
    
    # Status
    status = db.Column(
        db.String(20),
        default='active',
        nullable=False
    )  # active, inactive, discontinued
    
    # Audit
    created_by = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    # Relationships
    category = db.relationship('Category', back_populates='products')
    brand = db.relationship('Brand', back_populates='products')
    supplier = db.relationship('Supplier', back_populates='products')
    created_by_user = db.relationship('User', back_populates='created_products')
    inventory = db.relationship('Inventory', back_populates='product', uselist=False)
    sale_items = db.relationship('SaleItem', back_populates='product')
    purchase_items = db.relationship('PurchaseItem', back_populates='product')
    stock_movements = db.relationship('StockMovement', back_populates='product')
    
    @property
    def is_low_stock(self) -> bool:
        """Check if product is low on stock"""
        return self.quantity <= self.minimum_stock
    
    @property
    def is_out_of_stock(self) -> bool:
        """Check if product is out of stock"""
        return self.quantity == 0
    
    @property
    def profit_margin(self) -> float:
        """Calculate profit margin percentage"""
        if self.buying_price == 0:
            return 0
        return float((self.selling_price - self.buying_price) / self.buying_price * 100)
    
    def __repr__(self) -> str:
        return f"<Product {self.product_code} - {self.name}>"
