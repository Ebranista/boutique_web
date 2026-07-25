"""
Permission Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.permission_repository import PermissionRepository
from app.models.user import Permission


class PermissionService:
    """Permission service with business logic"""

    def __init__(self):
        self.permission_repository = PermissionRepository()

    def create_permission(self, data: Dict[str, Any]) -> Optional[Permission]:
        """Create a new permission"""
        if self.permission_repository.name_exists(data['name']):
            raise ValueError('Permission name already exists')

        return self.permission_repository.create(**data)

    def update_permission(self, permission_id: str, data: Dict[str, Any]) -> Optional[Permission]:
        """Update an existing permission"""
        if 'name' in data and self.permission_repository.name_exists(
            data['name'], permission_id
        ):
            raise ValueError('Permission name already exists')

        return self.permission_repository.update(permission_id, **data)

    def delete_permission(self, permission_id: str) -> bool:
        """Delete a permission"""
        return self.permission_repository.delete(permission_id)

    def get_permission_by_id(self, permission_id: str) -> Optional[Permission]:
        """Get permission by ID"""
        return self.permission_repository.get_by_id(permission_id)

    def get_all_permissions(self, page: int = 1, per_page: int = 20) -> tuple[List[Permission], int]:
        """Get all permissions"""
        return self.permission_repository.get_all(page, per_page)
