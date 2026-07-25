"""
Response Utilities
"""
from flask import jsonify
from typing import Any, Optional
from decimal import Decimal
from datetime import datetime, date
import json


class JSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for Decimal and datetime objects"""
    
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


def serialize_data(value: Any) -> Any:
    """Recursively serialize values for JSON response."""
    from datetime import datetime, date
    from decimal import Decimal

    if isinstance(value, dict):
        return {k: serialize_data(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serialize_data(v) for v in value]
    if isinstance(value, tuple):
        return tuple(serialize_data(v) for v in value)
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return value


def success_response(
    message: str,
    data: Any = None,
    status_code: int = 200
) -> tuple:
    """
    Create a success response
    
    Args:
        message: Success message
        data: Response data
        status_code: HTTP status code
        
    Returns:
        JSON response tuple
    """
    response = {
        'success': True,
        'message': message
    }
    
    if data is not None:
        response['data'] = serialize_data(data)
    
    return response, status_code


def error_response(
    message: str,
    errors: Any = None,
    status_code: int = 400
) -> tuple:
    """
    Create an error response
    
    Args:
        message: Error message
        errors: Validation errors
        status_code: HTTP status code
        
    Returns:
        JSON response tuple
    """
    response = {
        'success': False,
        'message': message
    }
    
    if errors is not None:
        response['errors'] = errors
    
    return response, status_code


def paginated_response(
    items: list,
    total: int,
    page: int,
    per_page: int,
    message: str = 'Success'
) -> tuple:
    """
    Create a paginated response
    
    Args:
        items: List of items
        total: Total number of items
        page: Current page number
        per_page: Items per page
        message: Success message
        
    Returns:
        JSON response tuple
    """
    total_pages = (total + per_page - 1) // per_page if per_page > 0 else 0
    
    response = {
        'success': True,
        'message': message,
        'data': {
            'items': serialize_data(items),
            'pagination': {
                'total': total,
                'page': page,
                'per_page': per_page,
                'total_pages': total_pages,
                'has_next': page < total_pages,
                'has_prev': page > 1
            }
        }
    }
    
    return response, 200
