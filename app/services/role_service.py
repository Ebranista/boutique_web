"""
Role Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.role_repository import RoleRepository
from app.repositories.permission_repository import PermissionRepository
from app.models.user import Role
from app.extensions import db


class RoleService:
    """Role service with business logic"""

    def __init__(self):
        self.role_repository = RoleRepository()
        self.permission_repository = PermissionRepository()

    def create_role(self, data: Dict[str, Any]) -> Optional[Role]:
        """Create a new role"""
        if self.role_repository.name_exists(data['name']):
            raise ValueError('Role name already exists')

        role = Role(
            name=data['name'],
            description=data.get('description')
        )

        if 'permission_ids' in data:
            for permission_id in data['permission_ids']:
                permission = self.permission_repository.get_by_id(permission_id)
                if permission:
                    role.permissions.append(permission)

        db.session.add(role)
        db.session.commit()
        db.session.refresh(role)
        return role

    def update_role(self, role_id: str, data: Dict[str, Any]) -> Optional[Role]:
        """Update an existing role"""
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return None

        if 'name' in data and self.role_repository.name_exists(data['name'], role_id):
            raise ValueError('Role name already exists')

        if 'permission_ids' in data:
            role.permissions.clear()
            for permission_id in data['permission_ids']:
                permission = self.permission_repository.get_by_id(permission_id)
                if permission:
                    role.permissions.append(permission)

        if 'name' in data:
            role.name = data['name']
        if 'description' in data:
            role.description = data.get('description')

        db.session.commit()
        db.session.refresh(role)
        return role

    def delete_role(self, role_id: str) -> bool:
        """Delete a role"""
        return self.role_repository.delete(role_id)

    def get_role_by_id(self, role_id: str) -> Optional[Role]:
        """Get role by ID"""
        return self.role_repository.get_by_id(role_id)

    def get_all_roles(self, page: int = 1, per_page: int = 20) -> tuple[List[Role], int]:
        """Get all roles"""
        return self.role_repository.get_all(page, per_page)
