"""
Expense Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.expense_service import ExpenseService
from app.services.expense_category_service import ExpenseCategoryService
from app.schemas.expense import ExpenseCreateSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

# Create namespace
expenses_ns = Namespace('expenses', description='Expense operations')

expense_category_model = expenses_ns.model('ExpenseCategory', {
    'name': fields.String(required=True),
    'description': fields.String,
    'is_recurring': fields.Boolean
})

expense_create_model = expenses_ns.model('ExpenseCreate', {
    'name': fields.String(required=True),
    'description': fields.String,
    'category_id': fields.String(required=True),
    'amount': fields.Float(required=True),
    'expense_date': fields.DateTime,
    'is_recurring': fields.Boolean,
    'recurring_month': fields.Integer,
    'receipt_image': fields.String,
    'notes': fields.String
})


@expenses_ns.route('/categories')
class ExpenseCategoryList(Resource):
    """Expense category list endpoint"""
    
    @expenses_ns.doc('get_expense_categories')
    @token_required
    def get(self):
        """Get all expense categories"""
        try:
            expense_category_service = ExpenseCategoryService()
            categories = expense_category_service.get_all_categories()
            return success_response('Success', [cat.to_dict() for cat in categories])
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @expenses_ns.doc('create_expense_category')
    @permission_required('manage_expenses')
    @expenses_ns.expect(expense_category_model)
    def post(self):
        """Create a new expense category"""
        try:
            data = request.get_json()
            expense_category_service = ExpenseCategoryService()
            category = expense_category_service.create_category(data)
            return success_response('Expense category created successfully', category.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@expenses_ns.route('/categories/<string:category_id>')
class ExpenseCategoryDetail(Resource):
    """Expense category detail endpoint"""
    
    @expenses_ns.doc('get_expense_category')
    @token_required
    def get(self, category_id):
        """Get expense category by ID"""
        try:
            expense_category_service = ExpenseCategoryService()
            category = expense_category_service.get_category_by_id(category_id)
            if category:
                return success_response('Expense category retrieved', category.to_dict())
            return error_response('Expense category not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @expenses_ns.doc('update_expense_category')
    @permission_required('manage_expenses')
    @expenses_ns.expect(expense_category_model)
    def put(self, category_id):
        """Update expense category"""
        try:
            data = request.get_json()
            expense_category_service = ExpenseCategoryService()
            category = expense_category_service.update_category(category_id, data)
            if category:
                return success_response('Expense category updated successfully', category.to_dict())
            return error_response('Expense category not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @expenses_ns.doc('delete_expense_category')
    @permission_required('manage_expenses')
    def delete(self, category_id):
        """Delete expense category"""
        try:
            expense_category_service = ExpenseCategoryService()
            success = expense_category_service.delete_category(category_id)
            if success:
                return success_response('Expense category deleted successfully')
            return error_response('Expense category not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@expenses_ns.route('/')
class ExpenseList(Resource):
    """Expense list endpoint"""
    
    @expenses_ns.doc('get_expenses')
    @token_required
    def get(self):
        """Get all expenses"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            expense_service = ExpenseService()
            expenses, total = expense_service.get_all_expenses(page, per_page)
            
            return paginated_response(
                [expense.to_dict() for expense in expenses],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @expenses_ns.doc('create_expense')
    @permission_required('manage_expenses')
    @expenses_ns.expect(expense_create_model)
    def post(self):
        """Create a new expense"""
        try:
            from flask_jwt_extended import get_jwt_identity
            
            data = request.get_json()
            schema = ExpenseCreateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            expense_service = ExpenseService()
            user_id = get_jwt_identity()
            expense = expense_service.create_expense(data, user_id)
            
            return success_response('Expense created successfully', expense.to_dict(), 201)
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@expenses_ns.route('/<string:expense_id>')
class ExpenseDetail(Resource):
    """Expense detail endpoint"""
    
    @expenses_ns.doc('get_expense')
    @token_required
    def get(self, expense_id):
        """Get expense by ID"""
        try:
            expense_service = ExpenseService()
            expense = expense_service.get_expense_by_id(expense_id)
            if expense:
                return success_response('Expense retrieved', expense.to_dict())
            return error_response('Expense not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @expenses_ns.doc('update_expense')
    @permission_required('manage_expenses')
    @expenses_ns.expect(expense_create_model)
    def put(self, expense_id):
        """Update expense"""
        try:
            data = request.get_json()
            expense_service = ExpenseService()
            expense = expense_service.update_expense(expense_id, data)
            if expense:
                return success_response('Expense updated successfully', expense.to_dict())
            return error_response('Expense not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @expenses_ns.doc('delete_expense')
    @permission_required('manage_expenses')
    def delete(self, expense_id):
        """Delete expense"""
        try:
            expense_service = ExpenseService()
            success = expense_service.delete_expense(expense_id)
            if success:
                return success_response('Expense deleted successfully')
            return error_response('Expense not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)


@expenses_ns.route('/category/<string:category_id>')
class ExpensesByCategory(Resource):
    """Expenses by category endpoint"""
    
    @expenses_ns.doc('get_expenses_by_category')
    @token_required
    def get(self, category_id):
        """Get expenses by category"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            expense_service = ExpenseService()
            expenses, total = expense_service.get_by_category(category_id, page, per_page)
            
            return paginated_response(
                [expense.to_dict() for expense in expenses],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@expenses_ns.route('/month/<int:year>/<int:month>')
class ExpensesByMonth(Resource):
    """Expenses by month endpoint"""
    
    @expenses_ns.doc('get_expenses_by_month')
    @token_required
    def get(self, year, month):
        """Get expenses by month"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            expense_service = ExpenseService()
            expenses, total = expense_service.get_by_month(year, month, page, per_page)
            
            return paginated_response(
                [expense.to_dict() for expense in expenses],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@expenses_ns.route('/today')
class TodayExpenses(Resource):
    """Today's expenses endpoint"""
    
    @expenses_ns.doc('get_today_expenses')
    @token_required
    def get(self):
        """Get today's expenses"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            expense_service = ExpenseService()
            expenses, total = expense_service.get_today_expenses(page, per_page)
            
            return paginated_response(
                [expense.to_dict() for expense in expenses],
                total,
                page,
                per_page
            )
        except Exception as e:
            return error_response(str(e), status_code=500)
