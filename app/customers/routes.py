"""
Customer Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.customer_service import CustomerService
from app.schemas.customer import CustomerSchema, CustomerCreateSchema, CustomerUpdateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
customers_ns = Namespace('customers', description='Customer operations')

customer_create_model = customers_ns.model('CustomerCreate', {
    'name': fields.String(required=True),
    'phone': fields.String(required=True),
    'email': fields.String,
    'address': fields.String,
    'gender': fields.String,
    'birthday': fields.Date,
    'image': fields.String
})

customer_update_model = customers_ns.model('CustomerUpdate', {
    'name': fields.String,
    'phone': fields.String,
    'email': fields.String,
    'address': fields.String,
    'gender': fields.String,
    'birthday': fields.Date,
    'image': fields.String,
    'is_active': fields.Boolean
})


@customers_ns.route('/')
class CustomerList(Resource):
    """Customer list endpoint"""
    
    @customers_ns.doc('get_customers')
    @token_required
    def get(self):
        """Get all customers"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            customer_service = CustomerService()
            customers, total = customer_service.get_all_customers(page, per_page)
            
            return paginated_response(
                [customer.to_dict() for customer in customers],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @customers_ns.doc('create_customer')
    @permission_required('manage_customers')
    @customers_ns.expect(customer_create_model)
    def post(self):
        """Create a new customer"""
        try:
            data = request.get_json()
            schema = CustomerCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            customer_service = CustomerService()
            customer = customer_service.create_customer(data)
            return success_response('Customer created successfully', customer.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@customers_ns.route('/<string:customer_id>')
class CustomerDetail(Resource):
    """Customer detail endpoint"""
    
    @customers_ns.doc('get_customer')
    @token_required
    def get(self, customer_id):
        """Get customer by ID"""
        try:
            customer_service = CustomerService()
            customer = customer_service.get_customer_by_id(customer_id)
            if customer:
                return success_response('Customer retrieved', customer.to_dict())
            return error_response('Customer not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @customers_ns.doc('update_customer')
    @permission_required('manage_customers')
    @customers_ns.expect(customer_update_model)
    def put(self, customer_id):
        """Update customer"""
        try:
            data = request.get_json()
            schema = CustomerUpdateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            customer_service = CustomerService()
            customer = customer_service.update_customer(customer_id, data)
            if customer:
                return success_response('Customer updated successfully', customer.to_dict())
            return error_response('Customer not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @customers_ns.doc('delete_customer')
    @permission_required('manage_customers')
    def delete(self, customer_id):
        """Delete customer"""
        try:
            customer_service = CustomerService()
            success = customer_service.delete_customer(customer_id)
            if success:
                return success_response('Customer deleted successfully')
            return error_response('Customer not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@customers_ns.route('/search')
class CustomerSearch(Resource):
    """Customer search endpoint"""
    
    @customers_ns.doc('search_customers')
    @token_required
    def get(self):
        """Search customers"""
        try:
            search_term = request.args.get('q', '')
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            customer_service = CustomerService()
            customers, total = customer_service.search_customers(search_term, page, per_page)
            
            return paginated_response(
                [customer.to_dict() for customer in customers],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@customers_ns.route('/phone/<string:phone>')
class CustomerByPhone(Resource):
    """Customer by phone endpoint"""
    
    @customers_ns.doc('get_customer_by_phone')
    @token_required
    def get(self, phone):
        """Get customer by phone"""
        try:
            customer_service = CustomerService()
            customer = customer_service.get_customer_by_phone(phone)
            if customer:
                return success_response('Customer retrieved', customer.to_dict())
            return error_response('Customer not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
