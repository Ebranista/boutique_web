"""
Helper Utilities
"""
import uuid
from decimal import Decimal
from datetime import datetime
from typing import Any


def generate_unique_id() -> str:
    """
    Generate a unique ID
    
    Returns:
        Unique ID string
    """
    return str(uuid.uuid4())


def format_currency(amount: Any, currency_symbol: str = '$') -> str:
    """
    Format amount as currency
    
    Args:
        amount: Amount to format
        currency_symbol: Currency symbol
        
    Returns:
        Formatted currency string
    """
    if isinstance(amount, str):
        amount = Decimal(amount)
    return f"{currency_symbol}{amount:,.2f}"


def format_date(date: Any, format: str = '%Y-%m-%d') -> str:
    """
    Format date
    
    Args:
        date: Date to format
        format: Date format string
        
    Returns:
        Formatted date string
    """
    if isinstance(date, str):
        date = datetime.fromisoformat(date)
    return date.strftime(format)


def serialize_model(model) -> dict:
    """
    Serialize SQLAlchemy model to dictionary
    
    Args:
        model: SQLAlchemy model instance
        
    Returns:
        Dictionary representation
    """
    if hasattr(model, 'to_dict'):
        return model.to_dict()
    
    return {
        column.name: getattr(model, column.name)
        for column in model.__table__.columns
    }
