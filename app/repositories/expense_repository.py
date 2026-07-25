"""
Expense Repository
"""
from typing import Optional, List
from datetime import datetime
from app.repositories.base import BaseRepository
from app.models.expense import Expense
from app.extensions import db


class ExpenseRepository(BaseRepository[Expense]):
    """Expense repository with specific operations"""
    
    def __init__(self):
        super().__init__(Expense)
    
    def get_by_category(self, category_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get expenses by category"""
        query = self.model.query.filter_by(
            category_id=category_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_date_range(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        per_page: int = 20
    ) -> tuple[List[Expense], int]:
        """Get expenses by date range"""
        query = self.model.query.filter(
            self.model.expense_date >= start_date,
            self.model.expense_date <= end_date,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_month(self, year: int, month: int, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get expenses by month"""
        query = self.model.query.filter(
            db.extract('year', self.model.expense_date) == year,
            db.extract('month', self.model.expense_date) == month,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_recurring(self, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get recurring expenses"""
        query = self.model.query.filter_by(
            is_recurring=True,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_today_expenses(self, page: int = 1, per_page: int = 20) -> tuple[List[Expense], int]:
        """Get today's expenses"""
        from datetime import date
        today = date.today()
        query = self.model.query.filter(
            db.func.date(self.model.expense_date) == today,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
