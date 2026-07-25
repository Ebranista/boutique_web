"""
Customer Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.customer import Customer


class CustomerRepository(BaseRepository[Customer]):
    """Customer repository with specific operations"""
    
    def __init__(self):
        super().__init__(Customer)
    
    def get_by_phone(self, phone: str) -> Optional[Customer]:
        """Get customer by phone"""
        return self.model.query.filter_by(phone=phone).first()
    
    def get_by_email(self, email: str) -> Optional[Customer]:
        """Get customer by email"""
        return self.model.query.filter_by(email=email).first()
    
    def get_active_customers(self, page: int = 1, per_page: int = 20) -> tuple[List[Customer], int]:
        """Get all active customers"""
        query = self.model.query.filter_by(is_active=True, is_deleted=False)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def phone_exists(self, phone: str, exclude_id: str = None) -> bool:
        """Check if phone number exists"""
        query = self.model.query.filter_by(phone=phone)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def search_customers(self, search_term: str, page: int = 1, per_page: int = 20) -> tuple[List[Customer], int]:
        """Search customers by name or phone"""
        query = self.model.query.filter(
            (self.model.name.ilike(f'%{search_term}%')) |
            (self.model.phone.ilike(f'%{search_term}%')),
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_top_customers(self, limit: int = 10) -> List[Customer]:
        """Get top customers by total purchases"""
        from sqlalchemy import desc
        query = self.model.query.filter_by(is_deleted=False)
        # Order by total purchases (would need to join with sales)
        # For now, return all
        return query.limit(limit).all()
