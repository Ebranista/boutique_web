"""
Sale Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class SaleItemSchema(BaseSchema):
    """Sale item schema"""
    sale_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))
    unit_price = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    discount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    subtotal = fields.Decimal(dump_only=True, places=2)
    unit_cost = fields.Decimal(dump_only=True, places=2)
    cost = fields.Decimal(dump_only=True, places=2)
    profit = fields.Decimal(dump_only=True, places=2)
    
    class Meta:
        fields = (
            'id', 'sale_id', 'product_id', 'quantity',
            'unit_price', 'discount', 'subtotal',
            'unit_cost', 'cost', 'profit',
            'created_at', 'updated_at'
        )


class SaleSchema(BaseSchema):
    """Sale schema"""
    invoice_number = fields.Str(dump_only=True)
    receipt_number = fields.Str(dump_only=True)
    customer_id = fields.Str(allow_none=True)
    subtotal = fields.Decimal(dump_only=True, places=2)
    discount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    tax = fields.Decimal(dump_only=True, places=2)
    total = fields.Decimal(dump_only=True, places=2)
    payment_method = fields.Str(
        required=True,
        validate=validate.OneOf(['cash', 'card', 'mobile_money', 'bank_transfer'])
    )
    cash_received = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    change = fields.Decimal(dump_only=True, places=2)
    total_cost = fields.Decimal(dump_only=True, places=2)
    total_profit = fields.Decimal(dump_only=True, places=2)
    status = fields.Str(
        dump_only=True,
        validate=validate.OneOf(['pending', 'completed', 'cancelled', 'refunded'])
    )
    sale_date = fields.DateTime(dump_only=True)
    notes = fields.Str(allow_none=True)
    cashier_id = fields.Str(dump_only=True)
    
    # Nested fields
    items = fields.Nested(SaleItemSchema, many=True, dump_only=True)
    
    # Computed fields
    total_items = fields.Integer(dump_only=True)
    total_quantity = fields.Integer(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'invoice_number', 'receipt_number', 'customer_id',
            'subtotal', 'discount', 'tax', 'total',
            'payment_method', 'cash_received', 'change',
            'total_cost', 'total_profit', 'status',
            'sale_date', 'notes', 'cashier_id',
            'items', 'total_items', 'total_quantity',
            'created_at', 'updated_at'
        )


class SaleCreateSchema(Schema):
    """Sale creation schema"""
    customer_id = fields.Str(allow_none=True)
    discount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    payment_method = fields.Str(
        required=True,
        validate=validate.OneOf(['cash', 'card', 'mobile_money', 'bank_transfer'])
    )
    cash_received = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    notes = fields.Str(allow_none=True)
    items = fields.List(
        fields.Dict(keys=fields.Str(), values=fields.Raw()),
        required=True,
        validate=validate.Length(min=1)
    )
