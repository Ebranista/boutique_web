"""
Audit Log Repository
"""
from typing import Optional, List
from datetime import datetime
from app.repositories.base import BaseRepository
from app.models.audit import AuditLog


class AuditLogRepository(BaseRepository[AuditLog]):
    """Audit log repository with specific operations"""
    
    def __init__(self):
        super().__init__(AuditLog)
    
    def get_by_user(self, user_id: str, page: int = 1, per_page: int = 20) -> tuple[List[AuditLog], int]:
        """Get audit logs by user"""
        query = self.model.query.filter_by(
            user_id=user_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_action(self, action: str, page: int = 1, per_page: int = 20) -> tuple[List[AuditLog], int]:
        """Get audit logs by action"""
        query = self.model.query.filter_by(
            action=action,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_entity(self, entity_type: str, entity_id: str, page: int = 1, per_page: int = 20) -> tuple[List[AuditLog], int]:
        """Get audit logs by entity"""
        query = self.model.query.filter_by(
            entity_type=entity_type,
            entity_id=entity_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_date_range(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[AuditLog], int]:
        """Get audit logs by date range"""
        query = self.model.query.filter(
            self.model.created_at >= start_date,
            self.model.created_at <= end_date,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def create_log(
        self,
        user_id: str,
        username: str,
        action: str,
        entity_type: str,
        entity_id: str = None,
        old_value: str = None,
        new_value: str = None,
        ip_address: str = None,
        user_agent: str = None,
        request_method: str = None,
        request_path: str = None,
        status: str = 'success',
        error_message: str = None
    ) -> AuditLog:
        """Create an audit log entry"""
        return self.create(
            user_id=user_id,
            username=username,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            old_value=old_value,
            new_value=new_value,
            ip_address=ip_address,
            user_agent=user_agent,
            request_method=request_method,
            request_path=request_path,
            status=status,
            error_message=error_message
        )
