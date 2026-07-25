"""
Supplier Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class SupplierSchema(BaseSchema):
    """Supplier schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    contact_person = fields.Str(allow_none=True, validate=validate.Length(max=100))
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=20))
    email = fields.Email(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    tin_number = fields.Str(allow_none=True, validate=validate.Length(max=50))
    outstanding_balance = fields.Decimal(dump_only=True, places=2)
    is_active = fields.Boolean(dump_only=True)
    
    # Computed fields
    total_purchases = fields.Integer(dump_only=True)
    total_products_supplied = fields.Integer(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'name', 'contact_person', 'phone', 'email', 'address',
            'tin_number', 'outstanding_balance', 'is_active',
            'total_purchases', 'total_products_supplied',
            'created_at', 'updated_at'
        )


class SupplierCreateSchema(Schema):
    """Supplier creation schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    contact_person = fields.Str(allow_none=True, validate=validate.Length(max=100))
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=20))
    email = fields.Email(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    tin_number = fields.Str(allow_none=True, validate=validate.Length(max=50))


class SupplierUpdateSchema(Schema):
    """Supplier update schema"""
    name = fields.Str(validate=validate.Length(min=1, max=100))
    contact_person = fields.Str(allow_none=True, validate=validate.Length(max=100))
    phone = fields.Str(validate=validate.Length(min=10, max=20))
    email = fields.Email(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    tin_number = fields.Str(allow_none=True, validate=validate.Length(max=50))
    is_active = fields.Boolean()
