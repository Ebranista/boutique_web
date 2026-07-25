"""
Purchase Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class PurchaseItemSchema(BaseSchema):
    """Purchase item schema"""
    purchase_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))
    buying_price = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    discount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    subtotal = fields.Decimal(dump_only=True, places=2)
    
    class Meta:
        fields = (
            'id', 'purchase_id', 'product_id', 'quantity',
            'buying_price', 'discount', 'subtotal',
            'created_at', 'updated_at'
        )


class PurchaseSchema(BaseSchema):
    """Purchase schema"""
    purchase_number = fields.Str(dump_only=True)
    supplier_id = fields.Str(required=True)
    subtotal = fields.Decimal(dump_only=True, places=2)
    discount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    tax = fields.Decimal(dump_only=True, places=2)
    total = fields.Decimal(dump_only=True, places=2)
    payment_method = fields.Str(
        required=True,
        validate=validate.OneOf(['cash', 'bank_transfer', 'credit'])
    )
    paid_amount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    balance = fields.Decimal(dump_only=True, places=2)
    purchase_date = fields.DateTime(dump_only=True)
    status = fields.Str(
        dump_only=True,
        validate=validate.OneOf(['pending', 'completed', 'cancelled'])
    )
    notes = fields.Str(allow_none=True)
    receipt_image = fields.Str(allow_none=True)
    created_by = fields.Str(dump_only=True)
    
    # Nested fields
    items = fields.Nested(PurchaseItemSchema, many=True, dump_only=True)
    
    # Computed fields
    total_items = fields.Integer(dump_only=True)
    total_quantity = fields.Integer(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'purchase_number', 'supplier_id', 'subtotal', 'discount',
            'tax', 'total', 'payment_method', 'paid_amount', 'balance',
            'purchase_date', 'status', 'notes', 'receipt_image',
            'created_by', 'items', 'total_items', 'total_quantity',
            'created_at', 'updated_at'
        )


class PurchaseCreateSchema(Schema):
    """Purchase creation schema"""
    supplier_id = fields.Str(required=True)
    discount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    payment_method = fields.Str(
        required=True,
        validate=validate.OneOf(['cash', 'bank_transfer', 'credit'])
    )
    paid_amount = fields.Decimal(missing=0, places=2, validate=validate.Range(min=0))
    notes = fields.Str(allow_none=True)
    receipt_image = fields.Str(allow_none=True)
    items = fields.List(
        fields.Dict(keys=fields.Str(), values=fields.Raw()),
        required=True,
        validate=validate.Length(min=1)
    )
