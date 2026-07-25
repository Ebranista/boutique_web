"""
User Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.user_repository import UserRepository
from app.models.user import User, Role
from app.extensions import db


class UserService:
    """User service with business logic"""
    
    def __init__(self):
        self.user_repository = UserRepository()
    
    def create_user(self, data: Dict[str, Any]) -> Optional[User]:
        """
        Create a new user
        
        Args:
            data: User data
            
        Returns:
            Created user or None if validation fails
        """
        # Check if username exists
        if self.user_repository.username_exists(data['username']):
            raise ValueError('Username already exists')
        
        # Check if email exists
        if self.user_repository.email_exists(data['email']):
            raise ValueError('Email already exists')
        
        # Create user
        user = User(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data.get('phone'),
            address=data.get('address')
        )
        user.set_password(data['password'])
        
        # Assign roles
        if 'role_ids' in data:
            for role_id in data['role_ids']:
                role = Role.query.filter_by(id=role_id).first()
                if role:
                    user.roles.append(role)
        
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        
        return user
    
    def update_user(self, user_id: str, data: Dict[str, Any]) -> Optional[User]:
        """
        Update user
        
        Args:
            user_id: User ID
            data: User data to update
            
        Returns:
            Updated user or None
        """
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return None
        
        # Check username uniqueness
        if 'username' in data and self.user_repository.username_exists(
            data['username'], user_id
        ):
            raise ValueError('Username already exists')
        
        # Check email uniqueness
        if 'email' in data and self.user_repository.email_exists(
            data['email'], user_id
        ):
            raise ValueError('Email already exists')
        
        # Update fields
        for key, value in data.items():
            if key == 'role_ids':
                # Update roles
                user.roles.clear()
                for role_id in value:
                    role = Role.query.filter_by(id=role_id).first()
                    if role:
                        user.roles.append(role)
            elif key != 'password' and hasattr(user, key):
                setattr(user, key, value)
        
        db.session.commit()
        db.session.refresh(user)
        
        return user
    
    def delete_user(self, user_id: str) -> bool:
        """
        Delete user
        
        Args:
            user_id: User ID
            
        Returns:
            True if deleted
        """
        return self.user_repository.delete(user_id)
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        return self.user_repository.get_by_id(user_id)
    
    def get_all_users(
        self,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[User], int]:
        """Get all users"""
        return self.user_repository.get_all(page, per_page)
    
    def check_permission(self, user_id: str, permission_name: str) -> bool:
        """
        Check if user has permission
        
        Args:
            user_id: User ID
            permission_name: Permission name
            
        Returns:
            True if user has permission
        """
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.has_permission(permission_name)
        return False
    
    def check_role(self, user_id: str, role_name: str) -> bool:
        """
        Check if user has role
        
        Args:
            user_id: User ID
            role_name: Role name
            
        Returns:
            True if user has role
        """
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.has_role(role_name)
        return False
