"""
Brand Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.brand_repository import BrandRepository
from app.models.product import Brand


class BrandService:
    """Brand service with business logic"""
    
    def __init__(self):
        self.brand_repository = BrandRepository()
    
    def create_brand(self, data: Dict[str, Any]) -> Optional[Brand]:
        """
        Create a new brand
        
        Args:
            data: Brand data
            
        Returns:
            Created brand or None if validation fails
        """
        if self.brand_repository.name_exists(data['name']):
            raise ValueError('Brand name already exists')
        
        return self.brand_repository.create(**data)
    
    def update_brand(self, brand_id: str, data: Dict[str, Any]) -> Optional[Brand]:
        """
        Update brand
        
        Args:
            brand_id: Brand ID
            data: Brand data to update
            
        Returns:
            Updated brand or None
        """
        if 'name' in data and self.brand_repository.name_exists(
            data['name'], brand_id
        ):
            raise ValueError('Brand name already exists')
        
        return self.brand_repository.update(brand_id, **data)
    
    def delete_brand(self, brand_id: str) -> bool:
        """Delete brand"""
        return self.brand_repository.delete(brand_id)
    
    def get_brand_by_id(self, brand_id: str) -> Optional[Brand]:
        """Get brand by ID"""
        return self.brand_repository.get_by_id(brand_id)
    
    def get_all_brands(self, page: int = 1, per_page: int = 20) -> tuple[List[Brand], int]:
        """Get all brands"""
        return self.brand_repository.get_all(page, per_page)
