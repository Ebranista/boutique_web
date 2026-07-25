"""
Base Service with Common Operations
"""
from typing import TypeVar, Generic, Optional, List, Dict, Any
from app.repositories.base import BaseRepository
from app.models.base import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseService(Generic[T]):
    """Base service with common operations"""
    
    def __init__(self, repository: BaseRepository[T]):
        """
        Initialize service with repository
        
        Args:
            repository: Repository instance
        """
        self.repository = repository
    
    def create(self, **kwargs) -> T:
        """
        Create a new record
        
        Args:
            **kwargs: Model attributes
            
        Returns:
            Created model instance
        """
        return self.repository.create(**kwargs)
    
    def get_by_id(self, id: str) -> Optional[T]:
        """
        Get record by ID
        
        Args:
            id: Record ID
            
        Returns:
            Model instance or None
        """
        return self.repository.get_by_id(id)
    
    def get_all(
        self,
        page: int = 1,
        per_page: int = 20,
        filters: Dict[str, Any] = None
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
        return self.repository.get_all(page, per_page, filters)
    
    def update(self, id: str, **kwargs) -> Optional[T]:
        """
        Update a record
        
        Args:
            id: Record ID
            **kwargs: Attributes to update
            
        Returns:
            Updated model instance or None
        """
        return self.repository.update(id, **kwargs)
    
    def delete(self, id: str) -> bool:
        """
        Soft delete a record
        
        Args:
            id: Record ID
            
        Returns:
            True if deleted, False otherwise
        """
        return self.repository.delete(id)
    
    def count(self, filters: Dict[str, Any] = None) -> int:
        """
        Count records
        
        Args:
            filters: Dictionary of filters
            
        Returns:
            Count of records
        """
        return self.repository.count(filters)
    
    def exists(self, id: str) -> bool:
        """
        Check if record exists
        
        Args:
            id: Record ID
            
        Returns:
            True if exists, False otherwise
        """
        return self.repository.exists(id)
