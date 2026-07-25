"""
Customer Service
"""
from typing import Optional, List, Dict, Any
from app.repositories.customer_repository import CustomerRepository
from app.models.customer import Customer


class CustomerService:
    """Customer service with business logic"""
    
    def __init__(self):
        self.customer_repository = CustomerRepository()
    
    def create_customer(self, data: Dict[str, Any]) -> Optional[Customer]:
        """
        Create a new customer
        
        Args:
            data: Customer data
            
        Returns:
            Created customer or None if validation fails
        """
        if self.customer_repository.phone_exists(data['phone']):
            raise ValueError('Phone number already exists')
        
        return self.customer_repository.create(**data)
    
    def update_customer(self, customer_id: str, data: Dict[str, Any]) -> Optional[Customer]:
        """
        Update customer
        
        Args:
            customer_id: Customer ID
            data: Customer data to update
            
        Returns:
            Updated customer or None
        """
        if 'phone' in data and self.customer_repository.phone_exists(
            data['phone'], customer_id
        ):
            raise ValueError('Phone number already exists')
        
        return self.customer_repository.update(customer_id, **data)
    
    def delete_customer(self, customer_id: str) -> bool:
        """Delete customer"""
        return self.customer_repository.delete(customer_id)
    
    def get_customer_by_id(self, customer_id: str) -> Optional[Customer]:
        """Get customer by ID"""
        return self.customer_repository.get_by_id(customer_id)
    
    def get_customer_by_phone(self, phone: str) -> Optional[Customer]:
        """Get customer by phone"""
        return self.customer_repository.get_by_phone(phone)
    
    def get_all_customers(self, page: int = 1, per_page: int = 20) -> tuple[List[Customer], int]:
        """Get all customers"""
        return self.customer_repository.get_all(page, per_page)
    
    def search_customers(self, search_term: str, page: int = 1, per_page: int = 20) -> tuple[List[Customer], int]:
        """Search customers"""
        return self.customer_repository.search_customers(search_term, page, per_page)
    
    def add_loyalty_points(self, customer_id: str, points: int) -> Optional[Customer]:
        """
        Add loyalty points to customer
        
        Args:
            customer_id: Customer ID
            points: Points to add
            
        Returns:
            Updated customer or None
        """
        customer = self.customer_repository.get_by_id(customer_id)
        if customer:
            customer.loyalty_points += points
            from app.extensions import db
            db.session.commit()
            db.session.refresh(customer)
        return customer
