"""
Inventory Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class InventorySchema(BaseSchema):
    """Inventory schema"""
    product_id = fields.Str(required=True)
    quantity = fields.Integer(dump_only=True)
    reserved_quantity = fields.Integer(dump_only=True)
    available_quantity = fields.Integer(dump_only=True)
    average_cost = fields.Decimal(dump_only=True, places=2)
    total_value = fields.Decimal(dump_only=True, places=2)
    
    # Computed fields
    is_low_stock = fields.Boolean(dump_only=True)
    is_out_of_stock = fields.Boolean(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'product_id', 'quantity', 'reserved_quantity',
            'available_quantity', 'average_cost', 'total_value',
            'is_low_stock', 'is_out_of_stock',
            'created_at', 'updated_at'
        )


class StockMovementSchema(BaseSchema):
    """Stock movement schema"""
    inventory_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    movement_type = fields.Str(
        required=True,
        validate=validate.OneOf(['stock_in', 'stock_out', 'adjustment', 'transfer'])
    )
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))
    previous_quantity = fields.Integer(dump_only=True)
    new_quantity = fields.Integer(dump_only=True)
    reference_type = fields.Str(allow_none=True)
    reference_id = fields.Str(allow_none=True)
    reason = fields.Str(allow_none=True, validate=validate.Length(max=255))
    notes = fields.Str(allow_none=True)
    performed_by = fields.Str(required=True)
    
    class Meta:
        fields = (
            'id', 'inventory_id', 'product_id', 'movement_type',
            'quantity', 'previous_quantity', 'new_quantity',
            'reference_type', 'reference_id', 'reason', 'notes',
            'performed_by', 'created_at', 'updated_at'
        )


class StockAdjustmentSchema(Schema):
    """Stock adjustment schema"""
    product_id = fields.Str(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))
    adjustment_type = fields.Str(
        required=True,
        validate=validate.OneOf(['add', 'subtract', 'set'])
    )
    reason = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    notes = fields.Str(allow_none=True)
