"""
Audit Log Model
"""
from datetime import datetime
from app.extensions import db
from .base import BaseModel


class AuditLog(BaseModel):
    """Audit log model for tracking system actions"""
    __tablename__ = 'audit_logs'
    
    # User
    user_id = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    )
    username = db.Column(db.String(50), nullable=False)
    
    # Action
    action = db.Column(db.String(50), nullable=False)  # create, update, delete, login, logout
    entity_type = db.Column(db.String(50), nullable=False)  # product, sale, user, etc.
    entity_id = db.Column(db.String(36))
    
    # Changes
    old_value = db.Column(db.Text)  # JSON string
    new_value = db.Column(db.Text)  # JSON string
    
    # Request Details
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(255))
    request_method = db.Column(db.String(10))
    request_path = db.Column(db.String(255))
    
    # Status
    status = db.Column(
        db.String(20),
        default='success',
        nullable=False
    )  # success, failure
    
    # Error
    error_message = db.Column(db.Text)
    
    def __repr__(self) -> str:
        return f"<AuditLog {self.action} {self.entity_type}>"
