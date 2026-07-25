"""
Expense Service
"""
from typing import Optional, List, Dict, Any
from decimal import Decimal
from datetime import datetime
from app.repositories.expense_repository import ExpenseRepository
from app.models.expense import Expense, ExpenseCategory
from app.extensions import db


class ExpenseService:
    """Expense service with business logic"""
    
    def __init__(self):
        self.expense_repository = ExpenseRepository()
    
    def create_expense(self, data: Dict[str, Any], created_by: str) -> Optional[Expense]:
        """
        Create a new expense
        
        Args:
            data: Expense data
            created_by: User ID who created the expense
            
        Returns:
            Created expense or None if validation fails
        """
        # Validate category
        category = ExpenseCategory.query.filter_by(id=data['category_id']).first()
        if not category:
            raise ValueError('Expense category not found')
        
        # Set expense date if not provided
        if 'expense_date' not in data:
            data['expense_date'] = datetime.utcnow()
        
        # Create expense
        expense = self.expense_repository.create(
            name=data['name'],
            description=data.get('description'),
            category_id=data['category_id'],
            amount=Decimal(str(data['amount'])),
            expense_date=data['expense_date'],
            is_recurring=data.get('is_recurring', False),
            recurring_month=data.get('recurring_month'),
            receipt_image=data.get('receipt_image'),
            notes=data.get('notes'),
            created_by=created_by
        )
        
        # Reduce capital
        from app.services.capital_service import CapitalService
        capital_service = CapitalService()
        capital_service.reduce_capital(Decimal(str(data['amount'])))
        
        return expense
    
    def update_expense(self, expense_id: str, data: Dict[str, Any]) -> Optional[Expense]:
        """
        Update expense
        
        Args:
            expense_id: Expense ID
            data: Expense data to update
            
        Returns:
            Updated expense or None
        """
        return self.expense_repository.update(expense_id, **data)
    
    def delete_expense(self, expense_id: str) -> bool:
        """Delete expense"""
        return self.expense_repository.delete(expense_id)
    
    def get_expense_by_id(self, expense_id: str) -> Optional[Expense]:
        """Get expense by ID"""
        return self.expense_repository.get_by_id(expense_id)
    
    def get_all_expenses(self, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get all expenses"""
        return self.expense_repository.get_all(page, per_page)
    
    def get_by_category(self, category_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get expenses by category"""
        return self.expense_repository.get_by_category(category_id, page, per_page)
    
    def get_by_month(self, year: int, month: int, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get expenses by month"""
        return self.expense_repository.get_by_month(year, month, page, per_page)
    
    def get_today_expenses(self, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get today's expenses"""
        return self.expense_repository.get_today_expenses(page, per_page)
