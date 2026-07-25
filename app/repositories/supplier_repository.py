"""
Supplier Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.supplier import Supplier


class SupplierRepository(BaseRepository[Supplier]):
    """Supplier repository with specific operations"""
    
    def __init__(self):
        super().__init__(Supplier)
    
    def get_by_name(self, name: str) -> Optional[Supplier]:
        """Get supplier by name"""
        return self.model.query.filter_by(name=name).first()
    
    def get_active_suppliers(self, page: int = 1, per_page: int = 20) -> tuple[List[Supplier], int]:
        """Get all active suppliers"""
        query = self.model.query.filter_by(is_active=True, is_deleted=False)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def name_exists(self, name: str, exclude_id: str = None) -> bool:
        """Check if supplier name exists"""
        query = self.model.query.filter_by(name=name)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def search_suppliers(self, search_term: str, page: int = 1, per_page: int = 20) -> tuple[List[Supplier], int]:
        """Search suppliers by name or phone"""
        query = self.model.query.filter(
            (self.model.name.ilike(f'%{search_term}%')) |
            (self.model.phone.ilike(f'%{search_term}%')),
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
