"""
Customer Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class CustomerSchema(BaseSchema):
    """Customer schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=20))
    email = fields.Email(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    gender = fields.Str(allow_none=True, validate=validate.OneOf(['male', 'female', 'other']))
    birthday = fields.Date(allow_none=True)
    image = fields.Str(allow_none=True)
    loyalty_points = fields.Integer(dump_only=True)
    is_active = fields.Boolean(dump_only=True)
    
    # Computed fields
    total_purchases = fields.Integer(dump_only=True)
    total_spent = fields.Decimal(dump_only=True, places=2)
    age = fields.Integer(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'name', 'phone', 'email', 'address', 'gender',
            'birthday', 'image', 'loyalty_points', 'is_active',
            'total_purchases', 'total_spent', 'age',
            'created_at', 'updated_at'
        )


class CustomerCreateSchema(Schema):
    """Customer creation schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=20))
    email = fields.Email(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    gender = fields.Str(allow_none=True, validate=validate.OneOf(['male', 'female', 'other']))
    birthday = fields.Date(allow_none=True)
    image = fields.Str(allow_none=True)


class CustomerUpdateSchema(Schema):
    """Customer update schema"""
    name = fields.Str(validate=validate.Length(min=1, max=100))
    phone = fields.Str(validate=validate.Length(min=10, max=20))
    email = fields.Email(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    gender = fields.Str(allow_none=True, validate=validate.OneOf(['male', 'female', 'other']))
    birthday = fields.Date(allow_none=True)
    image = fields.Str(allow_none=True)
    is_active = fields.Boolean()
