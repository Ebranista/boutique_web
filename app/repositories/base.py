"""
Base Repository with Common CRUD Operations
"""
from typing import List, Optional, Type, TypeVar, Generic
from sqlalchemy.orm import Query
from app.extensions import db
from app.models.base import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T]):
    """Base repository with common CRUD operations"""
    
    def __init__(self, model: Type[T]):
        """
        Initialize repository with model
        
        Args:
            model: SQLAlchemy model class
        """
        self.model = model
    
    def create(self, **kwargs) -> T:
        """
        Create a new record
        
        Args:
            **kwargs: Model attributes
            
        Returns:
            Created model instance
        """
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        return instance
    
    def get_by_id(self, id: str) -> Optional[T]:
        """
        Get record by ID
        
        Args:
            id: Record ID
            
        Returns:
            Model instance or None
        """
        return self.model.query.filter_by(id=id, is_deleted=False).first()
    
    def get_all(
        self,
        page: int = 1,
        per_page: int = 20,
        filters: dict = None
    ) -> tuple[List[T], int]:
        """
        Get all records with pagination
        
        Args:
            page: Page number
            per_page: Items per page
            filters: Dictionary of filters
            
        Returns:
            Tuple of (records, total_count)
        """
        query = self.model.query.filter_by(is_deleted=False)
        
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.filter(getattr(self.model, key) == value)
        
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def update(self, id: str, **kwargs) -> Optional[T]:
        """
        Update a record
        
        Args:
            id: Record ID
            **kwargs: Attributes to update
            
        Returns:
            Updated model instance or None
        """
        instance = self.get_by_id(id)
        if instance:
            for key, value in kwargs.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
            db.session.commit()
            db.session.refresh(instance)
        return instance
    
    def delete(self, id: str) -> bool:
        """
        Soft delete a record
        
        Args:
            id: Record ID
            
        Returns:
            True if deleted, False otherwise
        """
        instance = self.get_by_id(id)
        if instance:
            instance.soft_delete()
            db.session.commit()
            return True
        return False
    
    def hard_delete(self, id: str) -> bool:
        """
        Hard delete a record
        
        Args:
            id: Record ID
            
        Returns:
            True if deleted, False otherwise
        """
        instance = self.model.query.filter_by(id=id).first()
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return True
        return False
    
    def count(self, filters: dict = None) -> int:
        """
        Count records
        
        Args:
            filters: Dictionary of filters
            
        Returns:
            Count of records
        """
        query = self.model.query.filter_by(is_deleted=False)
        
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.filter(getattr(self.model, key) == value)
        
        return query.count()
    
    def exists(self, id: str) -> bool:
        """
        Check if record exists
        
        Args:
            id: Record ID
            
        Returns:
            True if exists, False otherwise
        """
        return self.get_by_id(id) is not None
    
    def get_by_field(self, field: str, value: any) -> Optional[T]:
        """
        Get record by field value
        
        Args:
            field: Field name
            value: Field value
            
        Returns:
            Model instance or None
        """
        if hasattr(self.model, field):
            return self.model.query.filter(
                getattr(self.model, field) == value,
                self.model.is_deleted == False
            ).first()
        return None
    
    def get_all_by_field(
        self,
        field: str,
        value: any,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[T], int]:
        """
        Get all records by field value
        
        Args:
            field: Field name
            value: Field value
            page: Page number
            per_page: Items per page
            
        Returns:
            Tuple of (records, total_count)
        """
        if hasattr(self.model, field):
            query = self.model.query.filter(
                getattr(self.model, field) == value,
                self.model.is_deleted == False
            )
            pagination = query.paginate(page=page, per_page=per_page, error_out=False)
            return pagination.items, pagination.total
        return [], 0
    
    def search(
        self,
        search_field: str,
        search_term: str,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[T], int]:
        """
        Search records by field
        
        Args:
            search_field: Field to search
            search_term: Search term
            page: Page number
            per_page: Items per page
            
        Returns:
            Tuple of (records, total_count)
        """
        if hasattr(self.model, search_field):
            query = self.model.query.filter(
                getattr(self.model, search_field).ilike(f'%{search_term}%'),
                self.model.is_deleted == False
            )
            pagination = query.paginate(page=page, per_page=per_page, error_out=False)
            return pagination.items, pagination.total
        return [], 0
