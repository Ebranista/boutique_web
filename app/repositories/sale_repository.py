"""
Sale Repository
"""
from typing import Optional, List
from datetime import datetime
from app.repositories.base import BaseRepository
from app.models.sale import Sale
from app.extensions import db


class SaleRepository(BaseRepository[Sale]):
    """Sale repository with specific operations"""
    
    def __init__(self):
        super().__init__(Sale)
    
    def get_by_invoice_number(self, invoice_number: str) -> Optional[Sale]:
        """Get sale by invoice number"""
        return self.model.query.filter_by(invoice_number=invoice_number).first()
    
    def get_by_receipt_number(self, receipt_number: str) -> Optional[Sale]:
        """Get sale by receipt number"""
        return self.model.query.filter_by(receipt_number=receipt_number).first()
    
    def get_by_customer(self, customer_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get sales by customer"""
        query = self.model.query.filter_by(
            customer_id=customer_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_cashier(self, cashier_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get sales by cashier"""
        query = self.model.query.filter_by(
            cashier_id=cashier_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_status(self, status: str, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get sales by status"""
        query = self.model.query.filter_by(
            status=status,
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
    ) -> tuple[List[Sale], int]:
        """Get sales by date range"""
        query = self.model.query.filter(
            self.model.sale_date >= start_date,
            self.model.sale_date <= end_date,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_today_sales(self, page: int = 1, per_page: int = 20) -> tuple[List[Sale], int]:
        """Get today's sales"""
        from datetime import date
        today = date.today()
        query = self.model.query.filter(
            db.func.date(self.model.sale_date) == today,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def invoice_number_exists(self, invoice_number: str, exclude_id: str = None) -> bool:
        """Check if invoice number exists"""
        query = self.model.query.filter_by(invoice_number=invoice_number)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
    
    def receipt_number_exists(self, receipt_number: str, exclude_id: str = None) -> bool:
        """Check if receipt number exists"""
        query = self.model.query.filter_by(receipt_number=receipt_number)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
