"""
Supplier Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.supplier_repository import SupplierRepository
from app.models.supplier import Supplier


class SupplierService:
    """Supplier service with business logic"""
    
    def __init__(self):
        self.supplier_repository = SupplierRepository()
    
    def create_supplier(self, data: Dict[str, Any]) -> Optional[Supplier]:
        """
        Create a new supplier
        
        Args:
            data: Supplier data
            
        Returns:
            Created supplier or None if validation fails
        """
        if self.supplier_repository.name_exists(data['name']):
            raise ValueError('Supplier name already exists')
        
        return self.supplier_repository.create(**data)
    
    def update_supplier(self, supplier_id: str, data: Dict[str, Any]) -> Optional[Supplier]:
        """
        Update supplier
        
        Args:
            supplier_id: Supplier ID
            data: Supplier data to update
            
        Returns:
            Updated supplier or None
        """
        if 'name' in data and self.supplier_repository.name_exists(
            data['name'], supplier_id
        ):
            raise ValueError('Supplier name already exists')
        
        return self.supplier_repository.update(supplier_id, **data)
    
    def delete_supplier(self, supplier_id: str) -> bool:
        """Delete supplier"""
        return self.supplier_repository.delete(supplier_id)
    
    def get_supplier_by_id(self, supplier_id: str) -> Optional[Supplier]:
        """Get supplier by ID"""
        return self.supplier_repository.get_by_id(supplier_id)
    
    def get_all_suppliers(self, page: int = 1, per_page: int = 20) -> tuple[List[Supplier], int]:
        """Get all suppliers"""
        return self.supplier_repository.get_all(page, per_page)
    
    def search_suppliers(self, search_term: str, page: int = 1, per_page: int = 20) -> tuple[List[Supplier], int]:
        """Search suppliers"""
        return self.supplier_repository.search_suppliers(search_term, page, per_page)
