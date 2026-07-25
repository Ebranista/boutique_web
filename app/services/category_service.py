"""
Category Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.category_repository import CategoryRepository
from app.models.product import Category


class CategoryService:
    """Category service with business logic"""
    
    def __init__(self):
        self.category_repository = CategoryRepository()
    
    def create_category(self, data: Dict[str, Any]) -> Optional[Category]:
        """
        Create a new category
        
        Args:
            data: Category data
            
        Returns:
            Created category or None if validation fails
        """
        if self.category_repository.name_exists(data['name']):
            raise ValueError('Category name already exists')
        
        return self.category_repository.create(**data)
    
    def update_category(self, category_id: str, data: Dict[str, Any]) -> Optional[Category]:
        """
        Update category
        
        Args:
            category_id: Category ID
            data: Category data to update
            
        Returns:
            Updated category or None
        """
        if 'name' in data and self.category_repository.name_exists(
            data['name'], category_id
        ):
            raise ValueError('Category name already exists')
        
        return self.category_repository.update(category_id, **data)
    
    def delete_category(self, category_id: str) -> bool:
        """Delete category"""
        return self.category_repository.delete(category_id)
    
    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        """Get category by ID"""
        return self.category_repository.get_by_id(category_id)
    
    def get_all_categories(self, page: int = 1, per_page: int = 20) -> tuple[List[Category], int]:
        """Get all categories"""
        return self.category_repository.get_all(page, per_page)
