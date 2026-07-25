"""
Notification Service
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from decimal import Decimal
from app.repositories.notification_repository import NotificationRepository
from app.models.notification import Notification
from app.extensions import db


class NotificationService:
    """Notification service with business logic"""
    
    def __init__(self):
        self.notification_repository = NotificationRepository()
    
    def create_notification(self, data: Dict[str, Any]) -> Optional[Notification]:
        """
        Create a new notification
        
        Args:
            data: Notification data
            
        Returns:
            Created notification or None
        """
        notification = self.notification_repository.create(**data)
        
        # Send push notification if Firebase is configured
        try:
            self.send_push_notification(notification)
        except Exception as e:
            # Log error but don't fail the notification creation
            print(f"Failed to send push notification: {e}")
        
        return notification
    
    def send_push_notification(self, notification: Notification) -> bool:
        """
        Send push notification via Firebase
        
        Args:
            notification: Notification object
            
        Returns:
            True if sent successfully
        """
        try:
            import firebase_admin
            from firebase_admin import messaging
            
            # Get user's FCM token (would need to store this in user model)
            # For now, this is a placeholder
            # In production, you would:
            # 1. Get user's FCM token from database
            # 2. Create and send message
            # 3. Update notification.push_sent and notification.push_sent_at
            
            notification.push_sent = True
            notification.push_sent_at = datetime.utcnow()
            db.session.commit()
            
            return True
        except Exception as e:
            print(f"Firebase push notification error: {e}")
            return False
    
    def create_low_stock_notification(self, user_id: str, product_name: str, quantity: int) -> Optional[Notification]:
        """
        Create low stock notification
        
        Args:
            user_id: User ID
            product_name: Product name
            quantity: Current quantity
            
        Returns:
            Created notification
        """
        return self.create_notification({
            'user_id': user_id,
            'title': 'Low Stock Alert',
            'message': f'Product {product_name} is running low on stock. Current quantity: {quantity}',
            'notification_type': 'low_stock',
            'reference_type': 'product',
            'reference_id': None
        })
    
    def create_out_of_stock_notification(self, user_id: str, product_name: str) -> Optional[Notification]:
        """
        Create out of stock notification
        
        Args:
            user_id: User ID
            product_name: Product name
            
        Returns:
            Created notification
        """
        return self.create_notification({
            'user_id': user_id,
            'title': 'Out of Stock Alert',
            'message': f'Product {product_name} is out of stock!',
            'notification_type': 'out_of_stock',
            'reference_type': 'product',
            'reference_id': None
        })
    
    def create_expense_reminder_notification(self, user_id: str, expense_name: str, amount: Decimal) -> Optional[Notification]:
        """
        Create expense reminder notification
        
        Args:
            user_id: User ID
            expense_name: Expense name
            amount: Expense amount
            
        Returns:
            Created notification
        """
        return self.create_notification({
            'user_id': user_id,
            'title': 'Expense Reminder',
            'message': f'Reminder: {expense_name} of {amount} is due',
            'notification_type': 'expense_reminder',
            'reference_type': 'expense',
            'reference_id': None
        })
    
    def get_user_notifications(self, user_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Notification], int]:
        """Get notifications for user"""
        return self.notification_repository.get_by_user(user_id, page, per_page)
    
    def get_unread_notifications(self, user_id: str, page: int = 1, per_page: int = 20) -> tuple[List[Notification], int]:
        """Get unread notifications for user"""
        return self.notification_repository.get_unread(user_id, page, per_page)
    
    def mark_as_read(self, notification_id: str) -> Optional[Notification]:
        """Mark notification as read"""
        return self.notification_repository.mark_as_read(notification_id)
    
    def mark_all_as_read(self, user_id: str) -> int:
        """Mark all notifications as read for user"""
        return self.notification_repository.mark_all_as_read(user_id)
