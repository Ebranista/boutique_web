"""
Marshmallow Schemas Package
"""
from .base import BaseSchema
from .user import UserSchema, UserCreateSchema, UserUpdateSchema, RoleSchema, PermissionSchema
from .product import ProductSchema, ProductCreateSchema, ProductUpdateSchema, CategorySchema, BrandSchema
from .supplier import SupplierSchema, SupplierCreateSchema, SupplierUpdateSchema
from .customer import CustomerSchema, CustomerCreateSchema, CustomerUpdateSchema
from .inventory import InventorySchema, StockMovementSchema
from .purchase import PurchaseSchema, PurchaseCreateSchema, PurchaseItemSchema
from .sale import SaleSchema, SaleCreateSchema, SaleItemSchema
from .expense import ExpenseSchema, ExpenseCreateSchema, ExpenseCategorySchema
from .capital import CapitalSchema
from .notification import NotificationSchema
from .setting import SettingSchema
from .audit import AuditLogSchema

__all__ = [
    'BaseSchema',
    'UserSchema',
    'UserCreateSchema',
    'UserUpdateSchema',
    'RoleSchema',
    'PermissionSchema',
    'ProductSchema',
    'ProductCreateSchema',
    'ProductUpdateSchema',
    'CategorySchema',
    'BrandSchema',
    'SupplierSchema',
    'SupplierCreateSchema',
    'SupplierUpdateSchema',
    'CustomerSchema',
    'CustomerCreateSchema',
    'CustomerUpdateSchema',
    'InventorySchema',
    'StockMovementSchema',
    'PurchaseSchema',
    'PurchaseCreateSchema',
    'PurchaseItemSchema',
    'SaleSchema',
    'SaleCreateSchema',
    'SaleItemSchema',
    'ExpenseSchema',
    'ExpenseCreateSchema',
    'ExpenseCategorySchema',
    'CapitalSchema',
    'NotificationSchema',
    'SettingSchema',
    'AuditLogSchema'
]
