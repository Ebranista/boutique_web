"""
User Management Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService
from app.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, admin_required

# Create namespace
users_ns = Namespace('users', description='User management operations')

# Define models
user_create_model = users_ns.model('UserCreate', {
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'phone': fields.String,
    'address': fields.String,
    'role_ids': fields.List(fields.String, required=True)
})

user_update_model = users_ns.model('UserUpdate', {
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'phone': fields.String,
    'address': fields.String,
    'profile_image': fields.String,
    'is_active': fields.Boolean,
    'role_ids': fields.List(fields.String)
})


@users_ns.route('/')
class UserList(Resource):
    """User list endpoint"""
    
    @users_ns.doc('get_users')
    @token_required
    def get(self):
        """Get all users"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            user_service = UserService()
            users, total = user_service.get_all_users(page, per_page)
            
            return paginated_response(
                [user.to_dict() for user in users],
                total,
                page,
                per_page
            )
            
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @users_ns.doc('create_user')
    @admin_required
    @users_ns.expect(user_create_model)
    def post(self):
        """Create a new user"""
        try:
            data = request.get_json()
            schema = UserCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            user_service = UserService()
            user = user_service.create_user(data)
            
            return success_response('User created successfully', user.to_dict(), 201)
            
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@users_ns.route('/<string:user_id>')
class UserDetail(Resource):
    """User detail endpoint"""
    
    @users_ns.doc('get_user')
    @token_required
    def get(self, user_id):
        """Get user by ID"""
        try:
            user_service = UserService()
            user = user_service.get_user_by_id(user_id)
            
            if user:
                return success_response('User retrieved', user.to_dict())
            else:
                return error_response('User not found', status_code=404)
                
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @users_ns.doc('update_user')
    @admin_required
    @users_ns.expect(user_update_model)
    def put(self, user_id):
        """Update user"""
        try:
            data = request.get_json()
            schema = UserUpdateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            user_service = UserService()
            user = user_service.update_user(user_id, data)
            
            if user:
                return success_response('User updated successfully', user.to_dict())
            else:
                return error_response('User not found', status_code=404)
                
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @users_ns.doc('delete_user')
    @admin_required
    def delete(self, user_id):
        """Delete user"""
        try:
            user_service = UserService()
            success = user_service.delete_user(user_id)
            
            if success:
                return success_response('User deleted successfully')
            else:
                return error_response('User not found', status_code=404)
                
        except Exception as e:
            return error_response(str(e), status_code=500)
