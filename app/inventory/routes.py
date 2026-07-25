"""
Inventory Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.inventory_service import InventoryService
from app.schemas.inventory import StockAdjustmentSchema, StockMovementSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
inventory_ns = Namespace('inventory', description='Inventory operations')

stock_adjustment_model = inventory_ns.model('StockAdjustment', {
    'product_id': fields.String(required=True),
    'quantity': fields.Integer(required=True),
    'adjustment_type': fields.String(required=True),
    'reason': fields.String(required=True),
    'notes': fields.String
})


@inventory_ns.route('/')
class InventoryList(Resource):
    """Inventory list endpoint"""
    
    @inventory_ns.doc('get_inventory')
    @token_required
    def get(self):
        """Get all inventory"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            inventory_service = InventoryService()
            # Get all products with their inventory
            from app.models.product import Product
            products = Product.query.filter_by(is_deleted=False).all()
            
            inventory_data = []
            for product in products:
                inventory = inventory_service.get_inventory_by_product(product.id)
                if inventory:
                    inv_dict = inventory.to_dict()
                    inv_dict['product_name'] = product.name
                    inv_dict['product_code'] = product.product_code
                    inventory_data.append(inv_dict)
            
            return paginated_response(
                inventory_data,
                len(inventory_data),
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@inventory_ns.route('/product/<string:product_id>')
class InventoryByProduct(Resource):
    """Inventory by product endpoint"""
    
    @inventory_ns.doc('get_inventory_by_product')
    @token_required
    def get(self, product_id):
        """Get inventory by product ID"""
        try:
            inventory_service = InventoryService()
            inventory = inventory_service.get_inventory_by_product(product_id)
            if inventory:
                return success_response('Inventory retrieved', inventory.to_dict())
            return error_response('Inventory not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@inventory_ns.route('/adjust')
class StockAdjustment(Resource):
    """Stock adjustment endpoint"""
    
    @inventory_ns.doc('adjust_stock')
    @permission_required('manage_inventory')
    @inventory_ns.expect(stock_adjustment_model)
    def post(self):
        """Adjust stock"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            data = request.get_json()
            schema = StockAdjustmentSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            inventory_service = InventoryService()
            user_id = get_jwt_identity()
            inventory = inventory_service.adjust_stock(
                product_id=data['product_id'],
                quantity=data['quantity'],
                adjustment_type=data['adjustment_type'],
                reason=data['reason'],
                performed_by=user_id,
                notes=data.get('notes')
            )
            
            if inventory:
                return success_response('Stock adjusted successfully', inventory.to_dict())
            return error_response('Stock adjustment failed', status_code=400)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@inventory_ns.route('/low-stock')
class LowStockInventory(Resource):
    """Low stock inventory endpoint"""
    
    @inventory_ns.doc('get_low_stock')
    @token_required
    def get(self):
        """Get low stock inventory"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            inventory_service = InventoryService()
            inventory, total = inventory_service.get_low_stock(page, per_page)
            
            return paginated_response(
                [inv.to_dict() for inv in inventory],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@inventory_ns.route('/out-of-stock')
class OutOfStockInventory(Resource):
    """Out of stock inventory endpoint"""
    
    @inventory_ns.doc('get_out_of_stock')
    @token_required
    def get(self):
        """Get out of stock inventory"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            inventory_service = InventoryService()
            inventory, total = inventory_service.get_out_of_stock(page, per_page)
            
            return paginated_response(
                [inv.to_dict() for inv in inventory],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@inventory_ns.route('/stock-movements')
class StockMovementHistory(Resource):
    """Stock movement history endpoint"""

    @inventory_ns.doc('get_stock_movements')
    @token_required
    def get(self):
        """Get stock movement history"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            product_id = request.args.get('product_id')
            inventory_id = request.args.get('inventory_id')

            inventory_service = InventoryService()
            movements, total = inventory_service.get_stock_movements(
                product_id=product_id,
                inventory_id=inventory_id,
                page=page,
                per_page=per_page
            )

            schema = StockMovementSchema(many=True)
            return paginated_response(
                schema.dump(movements),
                total,
                page,
                per_page,
                message='Stock movement history retrieved'
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
