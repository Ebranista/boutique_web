"""
User Schemas
"""
from marshmallow import Schema, fields, validate, post_load
from app.models.user import User, Role, Permission
from app.schemas.base import BaseSchema


class RoleSchema(BaseSchema):
    """Role schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(allow_none=True)
    
    class Meta:
        model = Role
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class PermissionSchema(BaseSchema):
    """Permission schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    module = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    
    class Meta:
        model = Permission
        fields = ('id', 'name', 'description', 'module', 'created_at', 'updated_at')


class UserSchema(BaseSchema):
    """User schema"""
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    phone = fields.Str(allow_none=True, validate=validate.Length(max=20))
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    profile_image = fields.Str(allow_none=True)
    is_active = fields.Boolean(dump_only=True)
    last_login = fields.DateTime(dump_only=True, allow_none=True)
    roles = fields.Nested(RoleSchema, many=True, dump_only=True)
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'phone', 'address', 'profile_image', 'is_active',
            'last_login', 'roles', 'created_at', 'updated_at'
        )


class UserCreateSchema(Schema):
    """User creation schema"""
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=validate.Length(min=8),
        load_only=True
    )
    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    phone = fields.Str(allow_none=True, validate=validate.Length(max=20))
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    role_ids = fields.List(fields.Str(), required=True)


class UserUpdateSchema(Schema):
    """User update schema"""
    email = fields.Email(validate=validate.Length(max=100))
    first_name = fields.Str(validate=validate.Length(min=1, max=50))
    last_name = fields.Str(validate=validate.Length(min=1, max=50))
    phone = fields.Str(allow_none=True, validate=validate.Length(max=20))
    address = fields.Str(allow_none=True, validate=validate.Length(max=255))
    profile_image = fields.Str(allow_none=True)
    is_active = fields.Boolean()
    role_ids = fields.List(fields.Str())


class ChangePasswordSchema(Schema):
    """Change password schema"""
    old_password = fields.Str(required=True, load_only=True)
    new_password = fields.Str(
        required=True,
        validate=validate.Length(min=8),
        load_only=True
    )


class LoginSchema(Schema):
    """Login schema"""
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
