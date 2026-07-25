"""
Notification Schema
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema


class NotificationSchema(BaseSchema):
    """Notification schema"""
    user_id = fields.Str(required=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    message = fields.Str(required=True)
    notification_type = fields.Str(
        required=True,
        validate=validate.OneOf([
            'low_stock', 'out_of_stock', 'expense_reminder',
            'purchase_completed', 'sale_completed', 'system'
        ])
    )
    reference_type = fields.Str(allow_none=True)
    reference_id = fields.Str(allow_none=True)
    is_read = fields.Boolean(dump_only=True)
    read_at = fields.DateTime(dump_only=True, allow_none=True)
    push_sent = fields.Boolean(dump_only=True)
    push_sent_at = fields.DateTime(dump_only=True, allow_none=True)
    
    # Computed fields
    is_unread = fields.Boolean(dump_only=True)
    
    class Meta:
        fields = (
            'id', 'user_id', 'title', 'message', 'notification_type',
            'reference_type', 'reference_id', 'is_read', 'read_at',
            'push_sent', 'push_sent_at', 'is_unread',
            'created_at', 'updated_at'
        )


class NotificationCreateSchema(Schema):
    """Notification creation schema"""
    user_id = fields.Str(required=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    message = fields.Str(required=True)
    notification_type = fields.Str(
        required=True,
        validate=validate.OneOf([
            'low_stock', 'out_of_stock', 'expense_reminder',
            'purchase_completed', 'sale_completed', 'system'
        ])
    )
    reference_type = fields.Str(allow_none=True)
    reference_id = fields.Str(allow_none=True)
