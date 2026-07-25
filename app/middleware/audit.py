"""
Audit Log Middleware
"""
from functools import wraps
from flask import request
from app.repositories.audit_repository import AuditLogRepository
from app.repositories.user_repository import UserRepository
import json


def audit_log(action: str, entity_type: str):
    """
    Decorator to log actions to audit trail
    
    Args:
        action: Action performed (create, update, delete, etc.)
        entity_type: Type of entity (product, sale, user, etc.)
        
    Returns:
        Decorated function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Get user info if authenticated
            user_id = None
            username = None
            
            try:
                from flask_jwt_extended import get_jwt_identity
                user_id = get_jwt_identity()
                if user_id:
                    user_repository = UserRepository()
                    user = user_repository.get_by_id(user_id)
                    if user:
                        username = user.username
            except:
                pass
            
            # Execute the function
            result = f(*args, **kwargs)
            
            # Log the action
            try:
                audit_repository = AuditLogRepository()
                audit_repository.create_log(
                    user_id=user_id,
                    username=username or 'system',
                    action=action,
                    entity_type=entity_type,
                    entity_id=kwargs.get('id'),
                    ip_address=request.remote_addr,
                    user_agent=request.headers.get('User-Agent'),
                    request_method=request.method,
                    request_path=request.path
                )
            except Exception as e:
                # Log error but don't fail the request
                print(f"Audit log error: {e}")
            
            return result
        return decorated_function
    return decorator
