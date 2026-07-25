"""
Brand Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.brand_service import BrandService
from app.schemas.product import BrandSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
brands_ns = Namespace('brands', description='Brand operations')

brand_model = brands_ns.model('Brand', {
    'name': fields.String(required=True),
    'description': fields.String
})


@brands_ns.route('/')
class BrandList(Resource):
    """Brand list endpoint"""
    
    @brands_ns.doc('get_brands')
    @token_required
    def get(self):
        """Get all brands"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            brand_service = BrandService()
            brands, total = brand_service.get_all_brands(page, per_page)
            
            return paginated_response(
                [brand.to_dict() for brand in brands],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @brands_ns.doc('create_brand')
    @permission_required('manage_products')
    @brands_ns.expect(brand_model)
    def post(self):
        """Create a new brand"""
        try:
            data = request.get_json()
            brand_service = BrandService()
            brand = brand_service.create_brand(data)
            return success_response('Brand created successfully', brand.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@brands_ns.route('/<string:brand_id>')
class BrandDetail(Resource):
    """Brand detail endpoint"""
    
    @brands_ns.doc('get_brand')
    @token_required
    def get(self, brand_id):
        """Get brand by ID"""
        try:
            brand_service = BrandService()
            brand = brand_service.get_brand_by_id(brand_id)
            if brand:
                return success_response('Brand retrieved', brand.to_dict())
            return error_response('Brand not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @brands_ns.doc('update_brand')
    @permission_required('manage_products')
    @brands_ns.expect(brand_model)
    def put(self, brand_id):
        """Update brand"""
        try:
            data = request.get_json()
            brand_service = BrandService()
            brand = brand_service.update_brand(brand_id, data)
            if brand:
                return success_response('Brand updated successfully', brand.to_dict())
            return error_response('Brand not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @brands_ns.doc('delete_brand')
    @permission_required('manage_products')
    def delete(self, brand_id):
        """Delete brand"""
        try:
            brand_service = BrandService()
            success = brand_service.delete_brand(brand_id)
            if success:
                return success_response('Brand deleted successfully')
            return error_response('Brand not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
