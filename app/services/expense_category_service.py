"""
Expense Category Service
"""
from app.models.expense import ExpenseCategory
from app.repositories.expense_category_repository import ExpenseCategoryRepository


class ExpenseCategoryService:
    """Service for expense category operations"""
    
    def __init__(self):
        self.repository = ExpenseCategoryRepository()
    
    def get_all_categories(self):
        """Get all expense categories"""
        return self.repository.get_all()
    
    def get_category_by_id(self, category_id):
        """Get expense category by ID"""
        return self.repository.get_by_id(category_id)
    
    def create_category(self, data):
        """Create a new expense category"""
        return self.repository.create(**data)
    
    def update_category(self, category_id, data):
        """Update expense category"""
        return self.repository.update(category_id, **data)
    
    def delete_category(self, category_id):
        """Delete expense category"""
        return self.repository.delete(category_id)
