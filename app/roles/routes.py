"""
Role management routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.role_service import RoleService
from app.schemas.user import RoleSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, admin_required

roles_ns = Namespace('roles', description='Role operations')

role_model = roles_ns.model('Role', {
    'name': fields.String(required=True),
    'description': fields.String,
    'permission_ids': fields.List(fields.String)
})


@roles_ns.route('/')
class RoleList(Resource):
    """Role list endpoint"""

    @roles_ns.doc('get_roles')
    @token_required
    def get(self):
        """Get all roles"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))

            role_service = RoleService()
            roles, total = role_service.get_all_roles(page, per_page)

            return paginated_response(
                [role.to_dict() for role in roles],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)

    @roles_ns.doc('create_role')
    @admin_required
    @roles_ns.expect(role_model)
    def post(self):
        """Create a new role"""
        try:
            data = request.get_json()
            role_service = RoleService()
            role = role_service.create_role(data)
            return success_response('Role created successfully', role.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@roles_ns.route('/<string:role_id>')
class RoleDetail(Resource):
    """Role detail endpoint"""

    @roles_ns.doc('get_role')
    @token_required
    def get(self, role_id):
        """Get role by ID"""
        try:
            role_service = RoleService()
            role = role_service.get_role_by_id(role_id)
            if role:
                return success_response('Role retrieved', role.to_dict())
            return error_response('Role not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @roles_ns.doc('update_role')
    @admin_required
    @roles_ns.expect(role_model)
    def put(self, role_id):
        """Update role"""
        try:
            data = request.get_json()
            role_service = RoleService()
            role = role_service.update_role(role_id, data)
            if role:
                return success_response('Role updated successfully', role.to_dict())
            return error_response('Role not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @roles_ns.doc('delete_role')
    @admin_required
    def delete(self, role_id):
        """Delete role"""
        try:
            role_service = RoleService()
            success = role_service.delete_role(role_id)
            if success:
                return success_response('Role deleted successfully')
            return error_response('Role not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
