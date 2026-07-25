"""
Purchase Repository
"""
from typing import Optional, List
from datetime import datetime
from app.repositories.base import BaseRepository
from app.models.purchase import Purchase


class PurchaseRepository(BaseRepository[Purchase]):
    """Purchase repository with specific operations"""
    
    def __init__(self):
        super().__init__(Purchase)
    
    def get_by_purchase_number(self, purchase_number: str) -> Optional[Purchase]:
        """Get purchase by purchase number"""
        return self.model.query.filter_by(purchase_number=purchase_number).first()
    
    def get_by_supplier(self, supplier_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Purchase], int]:
        """Get purchases by supplier"""
        query = self.model.query.filter_by(
            supplier_id=supplier_id,
            is_deleted=False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def get_by_status(self, status: str, page: int = 1, per_page: int = 20) -> tuple[List[Purchase], int]:
        """Get purchases by status"""
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
    ) -> tuple[List[Purchase], int]:
        """Get purchases by date range"""
        query = self.model.query.filter(
            self.model.purchase_date >= start_date,
            self.model.purchase_date <= end_date,
            self.model.is_deleted == False
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total
    
    def purchase_number_exists(self, purchase_number: str, exclude_id: str = None) -> bool:
        """Check if purchase number exists"""
        query = self.model.query.filter_by(purchase_number=purchase_number)
        if exclude_id:
            query = query.filter(self.model.id != exclude_id)
        return query.first() is not None
