"""
Audit Log Schema
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class AuditLogSchema(BaseSchema):
    """Audit log schema"""
    user_id = fields.Str(required=True)
    username = fields.Str(required=True)
    action = fields.Str(
        required=True,
        validate=validate.OneOf([
            'create', 'update', 'delete', 'login', 'logout',
            'sale', 'purchase', 'expense', 'inventory_update'
        ])
    )
    entity_type = fields.Str(required=True, validate=validate.Length(max=50))
    entity_id = fields.Str(allow_none=True)
    old_value = fields.Str(allow_none=True)
    new_value = fields.Str(allow_none=True)
    ip_address = fields.Str(allow_none=True, validate=validate.Length(max=45))
    user_agent = fields.Str(allow_none=True, validate=validate.Length(max=255))
    request_method = fields.Str(allow_none=True, validate=validate.Length(max=10))
    request_path = fields.Str(allow_none=True, validate=validate.Length(max=255))
    status = fields.Str(dump_only=True, validate=validate.OneOf(['success', 'failure']))
    error_message = fields.Str(allow_none=True)
    
    class Meta:
        fields = (
            'id', 'user_id', 'username', 'action', 'entity_type',
            'entity_id', 'old_value', 'new_value',
            'ip_address', 'user_agent', 'request_method', 'request_path',
            'status', 'error_message',
            'created_at', 'updated_at'
        )
