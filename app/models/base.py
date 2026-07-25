"""
Base Model with Common Fields
"""
from datetime import datetime
from app.extensions import db
import uuid


class BaseModel(db.Model):
    """Base model with common fields for all models"""
    __abstract__ = True
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    def soft_delete(self) -> None:
        """Soft delete the record"""
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()
    
    def restore(self) -> None:
        """Restore a soft-deleted record"""
        self.is_deleted = False
        self.deleted_at = None
    
    def to_dict(self) -> dict:
        """Convert model to dictionary"""
        from datetime import datetime, date
        from decimal import Decimal
        
        data = {}
        for column in self.__table__.columns:
            val = getattr(self, column.name)
            if isinstance(val, (datetime, date)):
                val = val.isoformat()
            elif isinstance(val, Decimal):
                val = float(val)
            data[column.name] = val
        return data
    
    def __repr__(self) -> str:
        """String representation of the model"""
        return f"<{self.__class__.__name__} {self.id}>"
