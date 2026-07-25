"""
Expense Category Repository
"""
from typing import Optional, List
from app.repositories.base import BaseRepository
from app.models.expense import ExpenseCategory


class ExpenseCategoryRepository(BaseRepository[ExpenseCategory]):
    """Expense category repository with specific operations"""
    
    def __init__(self):
        super().__init__(ExpenseCategory)
    
    def get_by_name(self, name: str) -> Optional[ExpenseCategory]:
        """Get expense category by name"""
        return self.model.query.filter_by(name=name).first()
    
    def name_exists(self, name: str, exclude_id: str = None) -> bool:
        """Check if expense category name exists"""
        query = self.model.query.filter_by(name=name)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def get_all(self) -> List[ExpenseCategory]:
        """Get all expense categories"""
        return self.model.query.filter_by(is_deleted=False).all()
