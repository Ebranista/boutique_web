"""
User Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository[User]):
    """User repository with specific operations"""
    
    def __init__(self):
        super().__init__(User)
    
    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        return self.model.query.filter_by(username=username).first()
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.model.query.filter_by(email=email).first()
    
    def get_by_username_or_email(self, identifier: str) -> Optional[User]:
        """Get user by username or email"""
        return self.model.query.filter(
            (self.model.username == identifier) | (self.model.email == identifier)
        ).first()
    
    def get_active_users(self, page: int = 1, per_page: int = 20) -> tuple[List[User], int]:
        """Get all active users"""
        query = self.model.query.filter_by(is_active=True, is_deleted=False)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_role(self, role_name: str, page: int = 1, per_page: int = 20) -> tuple[List[User], int]:
        """Get users by role"""
        from app.models.user import Role
        role = Role.query.filter_by(name=role_name).first()
        if role:
            query = role.users.filter(self.model.is_deleted == False)
            pagination = query.paginate(page=page, per_page=per_page, error_out=False)
            return pagination.items, pagination.total
        return [], 0
    
    def username_exists(self, username: str, exclude_id: str = None) -> bool:
        """Check if username exists"""
        query = self.model.query.filter_by(username=username)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def email_exists(self, email: str, exclude_id: str = None) -> bool:
        """Check if email exists"""
        query = self.model.query.filter_by(email=email)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
