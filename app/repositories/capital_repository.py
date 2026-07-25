"""
Capital Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.capital import Capital


class CapitalRepository(BaseRepository[Capital]):
    """Capital repository with specific operations"""
    
    def __init__(self):
        super().__init__(Capital)
    
    def get_active_capital(self) -> Optional[Capital]:
        """Get active capital record"""
        return self.model.query.filter_by(is_active=True).first()
    
    def get_capital_history(self, page: int = 1, per_page: int = 20) -> tuple[List[Capital], int]:
        """Get capital history"""
        query = self.model.query.filter_by(is_deleted=False)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
