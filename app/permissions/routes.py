"""
Permission management routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.permission_service import PermissionService
from app.schemas.user import PermissionSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, admin_required

permissions_ns = Namespace('permissions', description='Permission operations')

permission_model = permissions_ns.model('Permission', {
    'name': fields.String(required=True),
    'description': fields.String,
    'module': fields.String(required=True)
})


@permissions_ns.route('/')
class PermissionList(Resource):
    """Permission list endpoint"""

    @permissions_ns.doc('get_permissions')
    @token_required
    def get(self):
        """Get all permissions"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))

            permission_service = PermissionService()
            permissions, total = permission_service.get_all_permissions(page, per_page)

            return paginated_response(
                [permission.to_dict() for permission in permissions],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)

    @permissions_ns.doc('create_permission')
    @admin_required
    @permissions_ns.expect(permission_model)
    def post(self):
        """Create a new permission"""
        try:
            data = request.get_json()
            permission_service = PermissionService()
            permission = permission_service.create_permission(data)
            return success_response('Permission created successfully', permission.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@permissions_ns.route('/<string:permission_id>')
class PermissionDetail(Resource):
    """Permission detail endpoint"""

    @permissions_ns.doc('get_permission')
    @token_required
    def get(self, permission_id):
        """Get permission by ID"""
        try:
            permission_service = PermissionService()
            permission = permission_service.get_permission_by_id(permission_id)
            if permission:
                return success_response('Permission retrieved', permission.to_dict())
            return error_response('Permission not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @permissions_ns.doc('update_permission')
    @admin_required
    @permissions_ns.expect(permission_model)
    def put(self, permission_id):
        """Update permission"""
        try:
            data = request.get_json()
            permission_service = PermissionService()
            permission = permission_service.update_permission(permission_id, data)
            if permission:
                return success_response('Permission updated successfully', permission.to_dict())
            return error_response('Permission not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @permissions_ns.doc('delete_permission')
    @admin_required
    def delete(self, permission_id):
        """Delete permission"""
        try:
            permission_service = PermissionService()
            success = permission_service.delete_permission(permission_id)
            if success:
                return success_response('Permission deleted successfully')
            return error_response('Permission not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
