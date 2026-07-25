"""
Purchase Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.purchase_service import PurchaseService
from app.schemas.purchase import PurchaseCreateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
purchases_ns = Namespace('purchases', description='Purchase operations')

purchase_create_model = purchases_ns.model('PurchaseCreate', {
    'supplier_id': fields.String(required=True),
    'discount': fields.Float,
    'payment_method': fields.String(required=True),
    'paid_amount': fields.Float,
    'notes': fields.String,
    'receipt_image': fields.String,
    'items': fields.List(fields.Raw, required=True)
})


@purchases_ns.route('/')
class PurchaseList(Resource):
    """Purchase list endpoint"""
    
    @purchases_ns.doc('get_purchases')
    @token_required
    def get(self):
        """Get all purchases"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            purchase_service = PurchaseService()
            purchases, total = purchase_service.get_all_purchases(page, per_page)
            
            return paginated_response(
                [purchase.to_dict() for purchase in purchases],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @purchases_ns.doc('create_purchase')
    @permission_required('manage_purchases')
    @purchases_ns.expect(purchase_create_model)
    def post(self):
        """Create a new purchase"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            data = request.get_json()
            schema = PurchaseCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            purchase_service = PurchaseService()
            user_id = get_jwt_identity()
            purchase = purchase_service.create_purchase(data, user_id)
            
            return success_response('Purchase created successfully', purchase.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@purchases_ns.route('/<string:purchase_id>')
class PurchaseDetail(Resource):
    """Purchase detail endpoint"""
    
    @purchases_ns.doc('get_purchase')
    @token_required
    def get(self, purchase_id):
        """Get purchase by ID"""
        try:
            purchase_service = PurchaseService()
            purchase = purchase_service.get_purchase_by_id(purchase_id)
            if purchase:
                return success_response('Purchase retrieved', purchase.to_dict())
            return error_response('Purchase not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @purchases_ns.doc('update_purchase')
    @permission_required('manage_purchases')
    @purchases_ns.expect(purchase_create_model)
    def put(self, purchase_id):
        """Update purchase"""
        try:
            data = request.get_json()
            purchase_service = PurchaseService()
            purchase = purchase_service.update_purchase(purchase_id, data)
            if purchase:
                return success_response('Purchase updated successfully', purchase.to_dict())
            return error_response('Purchase not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)

    @purchases_ns.doc('delete_purchase')
    @permission_required('manage_purchases')
    def delete(self, purchase_id):
        """Delete purchase"""
        try:
            purchase_service = PurchaseService()
            success = purchase_service.delete_purchase(purchase_id)
            if success:
                return success_response('Purchase deleted successfully')
            return error_response('Purchase not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@purchases_ns.route('/<string:purchase_id>/complete')
class CompletePurchase(Resource):
    """Complete purchase endpoint"""
    
    @purchases_ns.doc('complete_purchase')
    @permission_required('manage_purchases')
    def post(self, purchase_id):
        """Complete a purchase"""
        try:
            purchase_service = PurchaseService()
            purchase = purchase_service.complete_purchase(purchase_id)
            if purchase:
                return success_response('Purchase completed successfully', purchase.to_dict())
            return error_response('Purchase not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@purchases_ns.route('/<string:purchase_id>/cancel')
class CancelPurchase(Resource):
    """Cancel purchase endpoint"""
    
    @purchases_ns.doc('cancel_purchase')
    @permission_required('manage_purchases')
    def post(self, purchase_id):
        """Cancel a purchase"""
        try:
            purchase_service = PurchaseService()
            purchase = purchase_service.cancel_purchase(purchase_id)
            if purchase:
                return success_response('Purchase cancelled successfully', purchase.to_dict())
            return error_response('Purchase not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@purchases_ns.route('/supplier/<string:supplier_id>')
class PurchasesBySupplier(Resource):
    """Purchases by supplier endpoint"""
    
    @purchases_ns.doc('get_purchases_by_supplier')
    @token_required
    def get(self, supplier_id):
        """Get purchases by supplier"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            purchase_service = PurchaseService()
            purchases, total = purchase_service.get_by_supplier(supplier_id, page, per_page)
            
            return paginated_response(
                [purchase.to_dict() for purchase in purchases],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
