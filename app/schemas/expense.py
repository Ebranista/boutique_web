"""
Expense Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class ExpenseCategorySchema(BaseSchema):
    """Expense category schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(allow_none=True)
    is_recurring = fields.Boolean(missing=False)
    
    class Meta:
        fields = (
            'id', 'name', 'description', 'is_recurring',
            'created_at', 'updated_at'
        )


class ExpenseSchema(BaseSchema):
    """Expense schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    category_id = fields.Str(required=True)
    amount = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    expense_date = fields.DateTime(dump_only=True)
    is_recurring = fields.Boolean(dump_only=True)
    recurring_month = fields.Integer(dump_only=True, allow_none=True)
    receipt_image = fields.Str(allow_none=True)
    notes = fields.Str(allow_none=True)
    created_by = fields.Str(dump_only=True)
    
    # Nested fields
    category = fields.Nested(ExpenseCategorySchema, dump_only=True)
    
    # Computed fields
    month = fields.Integer(dump_only=True)
    year = fields.Integer(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'name', 'description', 'category_id', 'amount',
            'expense_date', 'is_recurring', 'recurring_month',
            'receipt_image', 'notes', 'created_by',
            'category', 'month', 'year',
            'created_at', 'updated_at'
        )


class ExpenseCreateSchema(Schema):
    """Expense creation schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    category_id = fields.Str(required=True)
    amount = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    expense_date = fields.DateTime(allow_none=True)
    is_recurring = fields.Boolean(missing=False)
    recurring_month = fields.Integer(allow_none=True, validate=validate.Range(min=1, max=12))
    receipt_image = fields.Str(allow_none=True)
    notes = fields.Str(allow_none=True)
