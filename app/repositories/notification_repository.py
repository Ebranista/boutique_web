"""
Notification Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.notification import Notification
from app.extensions import db


class NotificationRepository(BaseRepository[Notification]):
    """Notification repository with specific operations"""
    
    def __init__(self):
        super().__init__(Notification)
    
    def get_by_user(self, user_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Notification], int]:
        """Get notifications by user"""
        query = self.model.query.filter_by(
            user_id=user_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_unread(self, user_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Notification], int]:
        """Get unread notifications for user"""
        query = self.model.query.filter_by(
            user_id=user_id,
            is_read=False,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_type(self, notification_type: str, page: int = 1, per_page: int = 20) -> tuple[List[Notification], int]:
        """Get notifications by type"""
        query = self.model.query.filter_by(
            notification_type=notification_type,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def mark_as_read(self, notification_id: str) -> Optional[Notification]:
        """Mark notification as read"""
        notification = self.get_by_id(notification_id)
        if notification:
            notification.mark_as_read()
            db.session.commit()
            db.session.refresh(notification)
        return notification
    
    def mark_all_as_read(self, user_id: str) -> int:
        """Mark all notifications as read for user"""
        from datetime import datetime
        count = self.model.query.filter_by(
            user_id=user_id,
            is_read=False,
            is_deleted=False
        ).update({
            'is_read': True,
            'read_at': datetime.utcnow()
        })
        db.session.commit()
        return count
