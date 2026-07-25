"""
Authentication Service
"""
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.extensions import db


class AuthService:
    """Authentication service for login, logout, token management"""
    
    def __init__(self):
        self.user_repository = UserRepository()
    
    def login(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """
        Authenticate user and generate tokens
        
        Args:
            username: Username or email
            password: User password
            
        Returns:
            Dictionary with tokens and user info, or None if authentication fails
        """
        user = self.user_repository.get_by_username_or_email(username)
        
        if not user or not user.check_password(password):
            return None
        
        if not user.is_active:
            return None
        
        # Update last login
        user.update_last_login()
        db.session.commit()
        
        # Generate tokens
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'roles': [role.name for role in user.roles]
            }
        }
    
    def refresh_token(self) -> Optional[str]:
        """
        Refresh access token
        
        Returns:
            New access token or None
        """
        current_user_id = get_jwt_identity()
        if current_user_id:
            return create_access_token(identity=current_user_id)
        return None
    
    def logout(self, token: str) -> bool:
        """
        Logout user (add token to blacklist)
        
        Args:
            token: JWT token
            
        Returns:
            True if logged out successfully
        """
        # In production, add token to blacklist using Redis
        # For now, return True
        return True
    
    def change_password(
        self,
        user_id: str,
        old_password: str,
        new_password: str
    ) -> bool:
        """
        Change user password
        
        Args:
            user_id: User ID
            old_password: Current password
            new_password: New password
            
        Returns:
            True if password changed successfully
        """
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return False
        
        if not user.check_password(old_password):
            return False
        
        user.set_password(new_password)
        db.session.commit()
        return True
    
    def get_current_user(self) -> Optional[User]:
        """
        Get current authenticated user
        
        Returns:
            Current user or None
        """
        current_user_id = get_jwt_identity()
        if current_user_id:
            return self.user_repository.get_by_id(current_user_id)
        return None
