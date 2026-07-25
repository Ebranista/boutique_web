"""
Audit Routes
"""
from flask import request
from flask_restx import Namespace, Resource
from app.repositories.audit_repository import AuditLogRepository
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, admin_required

# Create namespace
audit_ns = Namespace('audit', description='Audit log operations')


@audit_ns.route('/')
class AuditLogList(Resource):
    """Audit log list endpoint"""
    
    @audit_ns.doc('get_audit_logs')
    @admin_required
    def get(self):
        """Get all audit logs"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            audit_repository = AuditLogRepository()
            logs, total = audit_repository.get_all(page, per_page)
            
            return paginated_response(
                [log.to_dict() for log in logs],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@audit_ns.route('/user/<string:user_id>')
class AuditLogsByUser(Resource):
    """Audit logs by user endpoint"""
    
    @audit_ns.doc('get_audit_logs_by_user')
    @admin_required
    def get(self, user_id):
        """Get audit logs by user"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            audit_repository = AuditLogRepository()
            logs, total = audit_repository.get_by_user(user_id, page, per_page)
            
            return paginated_response(
                [log.to_dict() for log in logs],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@audit_ns.route('/action/<string:action>')
class AuditLogsByAction(Resource):
    """Audit logs by action endpoint"""
    
    @audit_ns.doc('get_audit_logs_by_action')
    @admin_required
    def get(self, action):
        """Get audit logs by action"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            audit_repository = AuditLogRepository()
            logs, total = audit_repository.get_by_action(action, page, per_page)
            
            return paginated_response(
                [log.to_dict() for log in logs],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@audit_ns.route('/entity/<string:entity_type>/<string:entity_id>')
class AuditLogsByEntity(Resource):
    """Audit logs by entity endpoint"""
    
    @audit_ns.doc('get_audit_logs_by_entity')
    @admin_required
    def get(self, entity_type, entity_id):
        """Get audit logs by entity"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            audit_repository = AuditLogRepository()
            logs, total = audit_repository.get_by_entity(entity_type, entity_id, page, per_page)
            
            return paginated_response(
                [log.to_dict() for log in logs],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
