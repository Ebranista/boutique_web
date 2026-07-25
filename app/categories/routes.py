"""
Category Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.category_service import CategoryService
from app.schemas.product import CategorySchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
categories_ns = Namespace('categories', description='Category operations')

category_model = categories_ns.model('Category', {
    'name': fields.String(required=True),
    'description': fields.String
})


@categories_ns.route('/')
class CategoryList(Resource):
    """Category list endpoint"""
    
    @categories_ns.doc('get_categories')
    @token_required
    def get(self):
        """Get all categories"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            category_service = CategoryService()
            categories, total = category_service.get_all_categories(page, per_page)
            
            return paginated_response(
                [category.to_dict() for category in categories],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @categories_ns.doc('create_category')
    @permission_required('manage_products')
    @categories_ns.expect(category_model)
    def post(self):
        """Create a new category"""
        try:
            data = request.get_json()
            category_service = CategoryService()
            category = category_service.create_category(data)
            return success_response('Category created successfully', category.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@categories_ns.route('/<string:category_id>')
class CategoryDetail(Resource):
    """Category detail endpoint"""
    
    @categories_ns.doc('get_category')
    @token_required
    def get(self, category_id):
        """Get category by ID"""
        try:
            category_service = CategoryService()
            category = category_service.get_category_by_id(category_id)
            if category:
                return success_response('Category retrieved', category.to_dict())
            return error_response('Category not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @categories_ns.doc('update_category')
    @permission_required('manage_products')
    @categories_ns.expect(category_model)
    def put(self, category_id):
        """Update category"""
        try:
            data = request.get_json()
            category_service = CategoryService()
            category = category_service.update_category(category_id, data)
            if category:
                return success_response('Category updated successfully', category.to_dict())
            return error_response('Category not found', status_code=404)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @categories_ns.doc('delete_category')
    @permission_required('manage_products')
    def delete(self, category_id):
        """Delete category"""
        try:
            category_service = CategoryService()
            success = category_service.delete_category(category_id)
            if success:
                return success_response('Category deleted successfully')
            return error_response('Category not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
