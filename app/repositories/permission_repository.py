"""
Permission Repository
"""
from typing import Optional
from app.repositories.base import BaseRepository
from app.models.user import Permission


class PermissionRepository(BaseRepository[Permission]):
    """Permission repository with specific operations"""

    def __init__(self):
        super().__init__(Permission)

    def get_by_name(self, name: str) -> Optional[Permission]:
        """Get permission by name"""
        return self.model.query.filter_by(name=name, is_deleted=False).first()

    def name_exists(self, name: str, exclude_id: str = None) -> bool:
        """Check if permission name exists"""
        query = self.model.query.filter_by(name=name, is_deleted=False)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
