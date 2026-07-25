"""
Capital Schema
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class CapitalSchema(BaseSchema):
    """Capital schema"""
    beginning_capital = fields.Decimal(dump_only=True, places=2)
    current_capital = fields.Decimal(dump_only=True, places=2)
    total_invested = fields.Decimal(dump_only=True, places=2)
    total_withdrawn = fields.Decimal(dump_only=True, places=2)
    period_start = fields.DateTime(dump_only=True)
    period_end = fields.DateTime(dump_only=True, allow_none=True)
    is_active = fields.Boolean(dump_only=True)
    
    # Computed fields
    capital_growth = fields.Float(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'beginning_capital', 'current_capital',
            'total_invested', 'total_withdrawn',
            'period_start', 'period_end', 'is_active',
            'capital_growth', 'created_at', 'updated_at'
        )


class CapitalInvestmentSchema(Schema):
    """Capital investment schema"""
    amount = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    notes = fields.Str(allow_none=True)


class CapitalWithdrawalSchema(Schema):
    """Capital withdrawal schema"""
    amount = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    notes = fields.Str(allow_none=True)
