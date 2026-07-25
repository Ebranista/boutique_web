"""
Notification Model
"""
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class Notification(BaseModel):
    """Notification model"""
    __tablename__ = 'notifications'
    
    # Recipient
    user_id = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    # Content
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(
        db.String(50),
        nullable=False
    )  # low_stock, out_of_stock, expense_reminder, etc.
    
    # Reference
    reference_type = db.Column(db.String(50))
    reference_id = db.Column(db.String(36))
    
    # Status
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    read_at = db.Column(db.DateTime)
    
    # Push Notification
    push_sent = db.Column(db.Boolean, default=False, nullable=False)
    push_sent_at = db.Column(db.DateTime)
    
    @property
    def is_unread(self) -> bool:
        """Check if notification is unread"""
        return not self.is_read
    
    def mark_as_read(self) -> None:
        """Mark notification as read"""
        self.is_read = True
        self.read_at = datetime.utcnow()
    
    def __repr__(self) -> str:
        return f"<Notification {self.title}>"
