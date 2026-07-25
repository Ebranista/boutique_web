"""
Product Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.product_service import ProductService
from app.schemas.product import ProductSchema, ProductCreateSchema, ProductUpdateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
products_ns = Namespace('products', description='Product operations')

# Define models
product_create_model = products_ns.model('ProductCreate', {
    'name': fields.String(required=True),
    'description': fields.String,
    'category_id': fields.String(required=True),
    'brand_id': fields.String(required=True),
    'gender': fields.String(required=True),
    'color': fields.String,
    'size': fields.String,
    'buying_price': fields.Float(required=True),
    'selling_price': fields.Float(required=True),
    'minimum_stock': fields.Integer,
    'supplier_id': fields.String,
    'image': fields.String
})

product_update_model = products_ns.model('ProductUpdate', {
    'name': fields.String,
    'description': fields.String,
    'category_id': fields.String,
    'brand_id': fields.String,
    'gender': fields.String,
    'color': fields.String,
    'size': fields.String,
    'buying_price': fields.Float,
    'selling_price': fields.Float,
    'minimum_stock': fields.Integer,
    'supplier_id': fields.String,
    'image': fields.String,
    'status': fields.String
})


@products_ns.route('/')
class ProductList(Resource):
    """Product list endpoint"""
    
    @products_ns.doc('get_products')
    @token_required
    def get(self):
        """Get all products"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            filters = {}
            if request.args.get('category_id'):
                filters['category_id'] = request.args.get('category_id')
            if request.args.get('brand_id'):
                filters['brand_id'] = request.args.get('brand_id')
            if request.args.get('gender'):
                filters['gender'] = request.args.get('gender')
            
            product_service = ProductService()
            products, total = product_service.get_all_products(page, per_page, filters)
            
            return paginated_response(
                [product.to_dict() for product in products],
                total,
                page,
                per_page
            )
            
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @products_ns.doc('create_product')
    @permission_required('manage_products')
    @products_ns.expect(product_create_model)
    def post(self):
        """Create a new product"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            data = request.get_json()
            schema = ProductCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            product_service = ProductService()
            user_id = get_jwt_identity()
            product = product_service.create_product(data, user_id)
            
            return success_response('Product created successfully', product.to_dict(), 201)
            
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@products_ns.route('/<string:product_id>')
class ProductDetail(Resource):
    """Product detail endpoint"""
    
    @products_ns.doc('get_product')
    @token_required
    def get(self, product_id):
        """Get product by ID"""
        try:
            product_service = ProductService()
            product = product_service.get_product_by_id(product_id)
            
            if product:
                return success_response('Product retrieved', product.to_dict())
            else:
                return error_response('Product not found', status_code=404)
                
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @products_ns.doc('update_product')
    @permission_required('manage_products')
    @products_ns.expect(product_update_model)
    def put(self, product_id):
        """Update product"""
        try:
            data = request.get_json()
            schema = ProductUpdateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            product_service = ProductService()
            product = product_service.update_product(product_id, data)
            
            if product:
                return success_response('Product updated successfully', product.to_dict())
            else:
                return error_response('Product not found', status_code=404)
                
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @products_ns.doc('delete_product')
    @permission_required('manage_products')
    def delete(self, product_id):
        """Delete product"""
        try:
            product_service = ProductService()
            success = product_service.delete_product(product_id)
            
            if success:
                return success_response('Product deleted successfully')
            else:
                return error_response('Product not found', status_code=404)
                
        except Exception as e:
            return error_response(str(e), status_code=500)


@products_ns.route('/search')
class ProductSearch(Resource):
    """Product search endpoint"""
    
    @products_ns.doc('search_products')
    @token_required
    def get(self):
        """Search products"""
        try:
            search_term = request.args.get('q', '')
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            product_service = ProductService()
            products, total = product_service.search_products(search_term, page, per_page)
            
            return paginated_response(
                [product.to_dict() for product in products],
                total,
                page,
                per_page
            )
            
        except Exception as e:
            return error_response(str(e), status_code=500)


@products_ns.route('/barcode/<string:barcode>')
class ProductByBarcode(Resource):
    """Product by barcode endpoint"""
    
    @products_ns.doc('get_product_by_barcode')
    @token_required
    def get(self, barcode):
        """Get product by barcode"""
        try:
            product_service = ProductService()
            product = product_service.get_product_by_barcode(barcode)
            
            if product:
                return success_response('Product retrieved', product.to_dict())
            else:
                return error_response('Product not found', status_code=404)
                
        except Exception as e:
            return error_response(str(e), status_code=500)


@products_ns.route('/low-stock')
class LowStockProducts(Resource):
    """Low stock products endpoint"""
    
    @products_ns.doc('get_low_stock_products')
    @token_required
    def get(self):
        """Get low stock products"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            product_service = ProductService()
            products, total = product_service.get_low_stock_products(page, per_page)
            
            return paginated_response(
                [product.to_dict() for product in products],
                total,
                page,
                per_page
            )
            
        except Exception as e:
            return error_response(str(e), status_code=500)


@products_ns.route('/out-of-stock')
class OutOfStockProducts(Resource):
    """Out of stock products endpoint"""
    
    @products_ns.doc('get_out_of_stock_products')
    @token_required
    def get(self):
        """Get out of stock products"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            product_service = ProductService()
            products, total = product_service.get_out_of_stock_products(page, per_page)
            
            return paginated_response(
                [product.to_dict() for product in products],
                total,
                page,
                per_page
            )
            
        except Exception as e:
            return error_response(str(e), status_code=500)
