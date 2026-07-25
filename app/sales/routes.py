"""
Sale Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.sale_service import SaleService
from app.schemas.sale import SaleCreateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
sales_ns = Namespace('sales', description='Sale operations')

sale_create_model = sales_ns.model('SaleCreate', {
    'customer_id': fields.String,
    'discount': fields.Float,
    'payment_method': fields.String(required=True),
    'cash_received': fields.Float,
    'notes': fields.String,
    'items': fields.List(fields.Raw, required=True)
})


@sales_ns.route('/')
class SaleList(Resource):
    """Sale list endpoint"""
    
    @sales_ns.doc('get_sales')
    @token_required
    def get(self):
        """Get all sales"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            sale_service = SaleService()
            sales, total = sale_service.get_all_sales(page, per_page)
            
            return paginated_response(
                [sale.to_dict() for sale in sales],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @sales_ns.doc('create_sale')
    @permission_required('manage_sales')
    @sales_ns.expect(sale_create_model)
    def post(self):
        """Create a new sale (POS)"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            data = request.get_json()
            schema = SaleCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            sale_service = SaleService()
            user_id = get_jwt_identity()
            sale = sale_service.create_sale(data, user_id)
            
            return success_response('Sale created successfully', sale.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@sales_ns.route('/<string:sale_id>')
class SaleDetail(Resource):
    """Sale detail endpoint"""
    
    @sales_ns.doc('get_sale')
    @token_required
    def get(self, sale_id):
        """Get sale by ID"""
        try:
            sale_service = SaleService()
            sale = sale_service.get_sale_by_id(sale_id)
            if sale:
                return success_response('Sale retrieved', sale.to_dict())
            return error_response('Sale not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @sales_ns.doc('update_sale')
    @permission_required('manage_sales')
    @sales_ns.expect(sale_create_model)
    def put(self, sale_id):
        """Update sale"""
        try:
            data = request.get_json()
            sale_service = SaleService()
            sale = sale_service.update_sale(sale_id, data)
            if sale:
                return success_response('Sale updated successfully', sale.to_dict())
            return error_response('Sale not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @sales_ns.doc('delete_sale')
    @permission_required('manage_sales')
    def delete(self, sale_id):
        """Delete sale"""
        try:
            sale_service = SaleService()
            success = sale_service.delete_sale(sale_id)
            if success:
                return success_response('Sale deleted successfully')
            return error_response('Sale not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@sales_ns.route('/<string:sale_id>/refund')
class RefundSale(Resource):
    """Refund sale endpoint"""
    
    @sales_ns.doc('refund_sale')
    @permission_required('manage_sales')
    def post(self, sale_id):
        """Refund a sale"""
        try:
            sale_service = SaleService()
            sale = sale_service.refund_sale(sale_id)
            if sale:
                return success_response('Sale refunded successfully', sale.to_dict())
            return error_response('Sale not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@sales_ns.route('/<string:sale_id>/cancel')
class CancelSale(Resource):
    """Cancel sale endpoint"""
    
    @sales_ns.doc('cancel_sale')
    @permission_required('manage_sales')
    def post(self, sale_id):
        """Cancel a sale"""
        try:
            sale_service = SaleService()
            sale = sale_service.cancel_sale(sale_id)
            if sale:
                return success_response('Sale cancelled successfully', sale.to_dict())
            return error_response('Sale not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@sales_ns.route('/today')
class TodaySales(Resource):
    """Today's sales endpoint"""
    
    @sales_ns.doc('get_today_sales')
    @token_required
    def get(self):
        """Get today's sales"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            sale_service = SaleService()
            sales, total = sale_service.get_today_sales(page, per_page)
            
            return paginated_response(
                [sale.to_dict() for sale in sales],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@sales_ns.route('/customer/<string:customer_id>')
class SalesByCustomer(Resource):
    """Sales by customer endpoint"""
    
    @sales_ns.doc('get_sales_by_customer')
    @token_required
    def get(self, customer_id):
        """Get sales by customer"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            sale_service = SaleService()
            sales, total = sale_service.get_by_customer(customer_id, page, per_page)
            
            return paginated_response(
                [sale.to_dict() for sale in sales],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
