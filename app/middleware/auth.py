"""
Authentication and Authorization Middleware
"""
from functools import wraps
from flask import jsonify, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from app.repositories.user_repository import UserRepository


def token_required(f):
    """
    Decorator to require JWT token
    
    Args:
        f: Function to decorate
        
    Returns:
        Decorated function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception as e:
            return {
                'success': False,
                'message': 'Authentication required',
                'error': str(e)
            }, 401
    return decorated_function


def permission_required(permission_name: str):
    """
    Decorator to require specific permission
    
    Args:
        permission_name: Name of the required permission
        
    Returns:
        Decorated function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                current_user_id = get_jwt_identity()
                
                user_repository = UserRepository()
                user = user_repository.get_by_id(current_user_id)
                
                if not user or not user.has_permission(permission_name):
                    return {
                        'success': False,
                        'message': f'Permission required: {permission_name}'
                    }, 403
                
                return f(*args, **kwargs)
            except Exception as e:
                return {
                    'success': False,
                    'message': 'Authentication required',
                    'error': str(e)
                }, 401
        return decorated_function
    return decorator


def role_required(role_name: str):
    """
    Decorator to require specific role
    
    Args:
        role_name: Name of the required role
        
    Returns:
        Decorated function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                current_user_id = get_jwt_identity()
                
                user_repository = UserRepository()
                user = user_repository.get_by_id(current_user_id)
                
                if not user or not user.has_role(role_name):
                    return {
                        'success': False,
                        'message': f'Role required: {role_name}'
                    }, 403
                
                return f(*args, **kwargs)
            except Exception as e:
                return {
                    'success': False,
                    'message': 'Authentication required',
                    'error': str(e)
                }, 401
        return decorated_function
    return decorator


def admin_required(f):
    """
    Decorator to require admin role
    
    Args:
        f: Function to decorate
        
    Returns:
        Decorated function
    """
    return role_required('Administrator')(f)
