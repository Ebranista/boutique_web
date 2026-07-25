"""
Role Repository
"""
from typing import Optional
from app.repositories.base import BaseRepository
from app.models.user import Role


class RoleRepository(BaseRepository[Role]):
    """Role repository with specific operations"""

    def __init__(self):
        super().__init__(Role)

    def get_by_name(self, name: str) -> Optional[Role]:
        """Get role by name"""
        return self.model.query.filter_by(name=name, is_deleted=False).first()

    def name_exists(self, name: str, exclude_id: str = None) -> bool:
        """Check if role name exists"""
        query = self.model.query.filter_by(name=name, is_deleted=False)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
