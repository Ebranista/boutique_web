"""
Capital Service
"""
from typing import Optional
from decimal import Decimal
from datetime import datetime
from app.repositories.capital_repository import CapitalRepository
from app.models.capital import Capital
from app.extensions import db


class CapitalService:
    """Capital service with business logic"""
    
    def __init__(self):
        self.capital_repository = CapitalRepository()
    
    def initialize_capital(self, beginning_capital: Decimal) -> Optional[Capital]:
        """
        Initialize capital for a new period
        
        Args:
            beginning_capital: Initial capital amount
            
        Returns:
            Created capital or None
        """
        # Check if active capital exists
        active_capital = self.capital_repository.get_active_capital()
        if active_capital:
            # Close current period
            active_capital.is_active = False
            active_capital.period_end = datetime.utcnow()
            db.session.commit()
        
        # Create new capital record
        capital = self.capital_repository.create(
            beginning_capital=beginning_capital,
            current_capital=beginning_capital,
            total_invested=beginning_capital,
            total_withdrawn=Decimal('0.00'),
            period_start=datetime.utcnow(),
            is_active=True
        )
        
        return capital
    
    def add_capital(self, amount: Decimal, notes: str = None) -> Optional[Capital]:
        """
        Add capital (investment)
        
        Args:
            amount: Amount to add
            notes: Notes
            
        Returns:
            Updated capital or None
        """
        capital = self.capital_repository.get_active_capital()
        if not capital:
            raise ValueError('No active capital period found')
        
        capital.total_invested += amount
        capital.current_capital += amount
        db.session.commit()
        db.session.refresh(capital)
        
        return capital
    
    def reduce_capital(self, amount: Decimal, notes: str = None) -> Optional[Capital]:
        """
        Reduce capital (withdrawal or expense)
        
        Args:
            amount: Amount to reduce
            notes: Notes
            
        Returns:
            Updated capital or None
        """
        capital = self.capital_repository.get_active_capital()
        if not capital:
            raise ValueError('No active capital period found')
        
        capital.total_withdrawn += amount
        capital.current_capital -= amount
        db.session.commit()
        db.session.refresh(capital)
        
        return capital
    
    def update_capital_from_sale(self, sale_amount: Decimal) -> Optional[Capital]:
        """
        Update capital from sale revenue
        
        Args:
            sale_amount: Sale amount
            
        Returns:
            Updated capital or None
        """
        capital = self.capital_repository.get_active_capital()
        if not capital:
            raise ValueError('No active capital period found')
        
        capital.current_capital += sale_amount
        db.session.commit()
        db.session.refresh(capital)
        
        return capital
    
    def get_current_capital(self) -> Optional[Capital]:
        """Get current active capital"""
        return self.capital_repository.get_active_capital()
    
    def get_capital_history(self, page: int = 1, per_page: int = 20):
        """Get capital history"""
        return self.capital_repository.get_capital_history(page, per_page)
