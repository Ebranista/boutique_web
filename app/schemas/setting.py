"""
Setting Schema
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class SettingSchema(BaseSchema):
    """Setting schema"""
    shop_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    logo = fields.Str(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    phone = fields.Str(allow_none=True, validate=validate.Length(max=20))
    email = fields.Email(allow_none=True)
    currency = fields.Str(missing='USD', validate=validate.Length(min=3, max=3))
    currency_symbol = fields.Str(missing='$', validate=validate.Length(max=5))
    tax_percentage = fields.Integer(missing=18, validate=validate.Range(min=0, max=100))
    receipt_footer = fields.Str(allow_none=True)
    receipt_header = fields.Str(allow_none=True)
    low_stock_limit = fields.Integer(missing=10, validate=validate.Range(min=0))
    dark_mode = fields.Boolean(missing=False)
    tin_number = fields.Str(allow_none=True, validate=validate.Length(max=50))
    
    class Meta:
        fields = (
            'id', 'shop_name', 'logo', 'address', 'phone', 'email',
            'currency', 'currency_symbol', 'tax_percentage',
            'receipt_footer', 'receipt_header', 'low_stock_limit',
            'dark_mode', 'tin_number',
            'created_at', 'updated_at'
        )


class SettingUpdateSchema(Schema):
    """Setting update schema"""
    shop_name = fields.Str(validate=validate.Length(min=1, max=100))
    logo = fields.Str(allow_none=True)
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    phone = fields.Str(allow_none=True, validate=validate.Length(max=20))
    email = fields.Email(allow_none=True)
    currency = fields.Str(validate=validate.Length(min=3, max=3))
    currency_symbol = fields.Str(validate=validate.Length(max=5))
    tax_percentage = fields.Integer(validate=validate.Range(min=0, max=100))
    receipt_footer = fields.Str(allow_none=True)
    receipt_header = fields.Str(allow_none=True)
    low_stock_limit = fields.Integer(validate=validate.Range(min=0))
    dark_mode = fields.Boolean()
    tin_number = fields.Str(allow_none=True, validate=validate.Length(max=50))
