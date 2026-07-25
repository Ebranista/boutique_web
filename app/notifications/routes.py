"""
Notification Routes
"""
from flask import request
from flask_restx import Namespace, Resource
from app.services.notification_service import NotificationService
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required

# Create namespace
notifications_ns = Namespace('notifications', description='Notification operations')


@notifications_ns.route('/')
class NotificationList(Resource):
    """Notification list endpoint"""
    
    @notifications_ns.doc('get_notifications')
    @token_required
    def get(self):
        """Get user notifications"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            user_id = get_jwt_identity()
            
            notification_service = NotificationService()
            notifications, total = notification_service.get_user_notifications(user_id, page, per_page)
            
            return paginated_response(
                [notification.to_dict() for notification in notifications],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@notifications_ns.route('/unread')
class UnreadNotifications(Resource):
    """Unread notifications endpoint"""
    
    @notifications_ns.doc('get_unread_notifications')
    @token_required
    def get(self):
        """Get unread notifications"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            user_id = get_jwt_identity()
            
            notification_service = NotificationService()
            notifications, total = notification_service.get_unread_notifications(user_id, page, per_page)
            
            return paginated_response(
                [notification.to_dict() for notification in notifications],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@notifications_ns.route('/<string:notification_id>/read')
class MarkAsRead(Resource):
    """Mark notification as read endpoint"""
    
    @notifications_ns.doc('mark_as_read')
    @token_required
    def post(self, notification_id):
        """Mark notification as read"""
        try:
            notification_service = NotificationService()
            notification = notification_service.mark_as_read(notification_id)
            if notification:
                return success_response('Notification marked as read', notification.to_dict())
            return error_response('Notification not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@notifications_ns.route('/read-all')
class MarkAllAsRead(Resource):
    """Mark all notifications as read endpoint"""
    
    @notifications_ns.doc('mark_all_as_read')
    @token_required
    def post(self):
        """Mark all notifications as read"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            user_id = get_jwt_identity()
            notification_service = NotificationService()
            count = notification_service.mark_all_as_read(user_id)
            return success_response(f'{count} notifications marked as read', {'count': count})
        except Exception as e:
            return error_response(str(e), status_code=500)
