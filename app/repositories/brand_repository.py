"""
Brand Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.product import Brand


class BrandRepository(BaseRepository[Brand]):
    """Brand repository with specific operations"""
    
    def __init__(self):
        super().__init__(Brand)
    
    def get_by_name(self, name: str) -> Optional[Brand]:
        """Get brand by name"""
        return self.model.query.filter_by(name=name).first()
    
    def name_exists(self, name: str, exclude_id: str = None) -> bool:
        """Check if brand name exists"""
        query = self.model.query.filter_by(name=name)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def get_with_product_count(self, page: int = 1, per_page: int = 20) -> tuple[List[Brand], int]:
        """Get brands with product count"""
        query = self.model.query.filter_by(is_deleted=False)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
