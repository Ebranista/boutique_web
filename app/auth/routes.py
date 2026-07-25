"""
Authentication Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.auth_service import AuthService
from app.schemas.user import LoginSchema, ChangePasswordSchema
from app.utils.response import success_response, error_response
from app.middleware.auth import token_required

# Create namespace
auth_ns = Namespace('auth', description='Authentication operations')

# Define models
login_model = auth_ns.model('Login', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

change_password_model = auth_ns.model('ChangePassword', {
    'old_password': fields.String(required=True),
    'new_password': fields.String(required=True)
})

refresh_token_model = auth_ns.model('RefreshToken', {
    'refresh_token': fields.String(required=True)
})


@auth_ns.route('/login')
class Login(Resource):
    """Login endpoint"""
    
    @auth_ns.doc('login')
    @auth_ns.expect(login_model)
    def post(self):
        """Login user and return tokens"""
        try:
            data = request.get_json()
            schema = LoginSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            auth_service = AuthService()
            result = auth_service.login(data['username'], data['password'])
            
            if result:
                return success_response('Login successful', result)
            else:
                return error_response('Invalid credentials', status_code=401)
                
        except Exception as e:
            return error_response(str(e), status_code=500)


@auth_ns.route('/refresh')
class RefreshToken(Resource):
    """Refresh access token"""
    
    @auth_ns.doc('refresh_token')
    def post(self):
        """Refresh access token"""
        try:
            auth_service = AuthService()
            access_token = auth_service.refresh_token()
            
            if access_token:
                return success_response('Token refreshed', {'access_token': access_token})
            else:
                return error_response('Invalid refresh token', status_code=401)
                
        except Exception as e:
            return error_response(str(e), status_code=500)


@auth_ns.route('/logout')
class Logout(Resource):
    """Logout endpoint"""
    
    @auth_ns.doc('logout')
    @token_required
    def post(self):
        """Logout user"""
        try:
            auth_service = AuthService()
            auth_service.logout(request.headers.get('Authorization'))
            return success_response('Logout successful')
            
        except Exception as e:
            return error_response(str(e), status_code=500)


@auth_ns.route('/change-password')
class ChangePassword(Resource):
    """Change password endpoint"""
    
    @auth_ns.doc('change_password')
    @token_required
    @auth_ns.expect(change_password_model)
    def post(self):
        """Change user password"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            data = request.get_json()
            schema = ChangePasswordSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            auth_service = AuthService()
            user_id = get_jwt_identity()
            success = auth_service.change_password(
                user_id,
                data['old_password'],
                data['new_password']
            )
            
            if success:
                return success_response('Password changed successfully')
            else:
                return error_response('Invalid old password', status_code=400)
                
        except Exception as e:
            return error_response(str(e), status_code=500)


@auth_ns.route('/me')
class CurrentUser(Resource):
    """Get current user"""
    
    @auth_ns.doc('get_current_user')
    @token_required
    def get(self):
        """Get current authenticated user"""
        try:
            auth_service = AuthService()
            user = auth_service.get_current_user()
            
            if user:
                return success_response('User retrieved', user.to_dict())
            else:
                return error_response('User not found', status_code=404)
                
        except Exception as e:
            return error_response(str(e), status_code=500)
