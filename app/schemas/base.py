"""
Base Schema with Common Fields
"""
from marshmallow import Schema, fields, validate


class BaseSchema(Schema):
    """Base schema with common fields"""
    id = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_deleted = fields.Boolean(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True, allow_none=True)


class SuccessResponseSchema(Schema):
    """Standard success response schema"""
    success = fields.Boolean(dump_only=True)
    message = fields.Str(dump_only=True)
    data = fields.Dict(dump_only=True, allow_none=True)


class ErrorResponseSchema(Schema):
    """Standard error response schema"""
    success = fields.Boolean(dump_only=True)
    message = fields.Str(dump_only=True)
    errors = fields.Dict(dump_only=True, allow_none=True)


class PaginationSchema(Schema):
    """Pagination schema"""
    page = fields.Integer(missing=1, validate=validate.Range(min=1))
    per_page = fields.Integer(
        missing=20,
        validate=validate.Range(min=1, max=100)
    )
