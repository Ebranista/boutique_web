"""
Supplier Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.supplier_service import SupplierService
from app.schemas.supplier import SupplierSchema, SupplierCreateSchema, SupplierUpdateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
suppliers_ns = Namespace('suppliers', description='Supplier operations')

supplier_create_model = suppliers_ns.model('SupplierCreate', {
    'name': fields.String(required=True),
    'contact_person': fields.String,
    'phone': fields.String(required=True),
    'email': fields.String,
    'address': fields.String,
    'tin_number': fields.String
})

supplier_update_model = suppliers_ns.model('SupplierUpdate', {
    'name': fields.String,
    'contact_person': fields.String,
    'phone': fields.String,
    'email': fields.String,
    'address': fields.String,
    'tin_number': fields.String,
    'is_active': fields.Boolean
})


@suppliers_ns.route('/')
class SupplierList(Resource):
    """Supplier list endpoint"""
    
    @suppliers_ns.doc('get_suppliers')
    @token_required
    def get(self):
        """Get all suppliers"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            supplier_service = SupplierService()
            suppliers, total = supplier_service.get_all_suppliers(page, per_page)
            
            return paginated_response(
                [supplier.to_dict() for supplier in suppliers],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @suppliers_ns.doc('create_supplier')
    @permission_required('manage_suppliers')
    @suppliers_ns.expect(supplier_create_model)
    def post(self):
        """Create a new supplier"""
        try:
            data = request.get_json()
            schema = SupplierCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            supplier_service = SupplierService()
            supplier = supplier_service.create_supplier(data)
            return success_response('Supplier created successfully', supplier.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@suppliers_ns.route('/<string:supplier_id>')
class SupplierDetail(Resource):
    """Supplier detail endpoint"""
    
    @suppliers_ns.doc('get_supplier')
    @token_required
    def get(self, supplier_id):
        """Get supplier by ID"""
        try:
            supplier_service = SupplierService()
            supplier = supplier_service.get_supplier_by_id(supplier_id)
            if supplier:
                return success_response('Supplier retrieved', supplier.to_dict())
            return error_response('Supplier not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @suppliers_ns.doc('update_supplier')
    @permission_required('manage_suppliers')
    @suppliers_ns.expect(supplier_update_model)
    def put(self, supplier_id):
        """Update supplier"""
        try:
            data = request.get_json()
            schema = SupplierUpdateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            supplier_service = SupplierService()
            supplier = supplier_service.update_supplier(supplier_id, data)
            if supplier:
                return success_response('Supplier updated successfully', supplier.to_dict())
            return error_response('Supplier not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @suppliers_ns.doc('delete_supplier')
    @permission_required('manage_suppliers')
    def delete(self, supplier_id):
        """Delete supplier"""
        try:
            supplier_service = SupplierService()
            success = supplier_service.delete_supplier(supplier_id)
            if success:
                return success_response('Supplier deleted successfully')
            return error_response('Supplier not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@suppliers_ns.route('/search')
class SupplierSearch(Resource):
    """Supplier search endpoint"""
    
    @suppliers_ns.doc('search_suppliers')
    @token_required
    def get(self):
        """Search suppliers"""
        try:
            search_term = request.args.get('q', '')
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            supplier_service = SupplierService()
            suppliers, total = supplier_service.search_suppliers(search_term, page, per_page)
            
            return paginated_response(
                [supplier.to_dict() for supplier in suppliers],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
