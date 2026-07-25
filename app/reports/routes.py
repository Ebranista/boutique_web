"""
Report Routes
"""
from flask import request
from flask_restx import Namespace, Resource
from app.services.report_service import ReportService
from app.utils.response import success_response, error_response
from app.middleware.auth import token_required, permission_required

# Create namespace
reports_ns = Namespace('reports', description='Report operations')


@reports_ns.route('/sales')
class ReportSales(Resource):
    """Sales report endpoint"""
    
    @reports_ns.doc('get_sales_report')
    @token_required
    def get(self):
        """Get sales report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            report_service = ReportService()
            report = report_service.get_sales_report(start_date.date(), end_date.date(), page, per_page)
            
            return success_response('Sales report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/purchases')
class ReportPurchases(Resource):
    """Purchase report endpoint"""
    
    @reports_ns.doc('get_purchase_report')
    @token_required
    def get(self):
        """Get purchase report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            report_service = ReportService()
            report = report_service.get_purchase_report(start_date.date(), end_date.date(), page, per_page)
            
            return success_response('Purchase report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/expenses')
class ReportExpenses(Resource):
    """Expense report endpoint"""
    
    @reports_ns.doc('get_expense_report')
    @token_required
    def get(self):
        """Get expense report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            report_service = ReportService()
            report = report_service.get_expense_report(start_date.date(), end_date.date(), page, per_page)
            
            return success_response('Expense report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/inventory')
class ReportInventory(Resource):
    """Inventory report endpoint"""
    
    @reports_ns.doc('get_inventory_report')
    @token_required
    def get(self):
        """Get inventory report"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            report_service = ReportService()
            report = report_service.get_inventory_report(page, per_page)
            
            return success_response('Inventory report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/profit')
class ReportProfit(Resource):
    """Profit report endpoint"""
    
    @reports_ns.doc('get_profit_report')
    @token_required
    def get(self):
        """Get profit report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            
            report_service = ReportService()
            report = report_service.get_profit_report(start_date.date(), end_date.date())
            
            return success_response('Profit report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/product-profit')
class ReportProductProfit(Resource):
    """Product profit report endpoint"""
    
    @reports_ns.doc('get_product_profit_report')
    @token_required
    def get(self):
        """Get product profit report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            limit = int(request.args.get('limit', 20))
            
            report_service = ReportService()
            report = report_service.get_product_profit_report(start_date.date(), end_date.date(), limit)
            
            return success_response('Product profit report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/customers')
class ReportCustomers(Resource):
    """Customer report endpoint"""
    
    @reports_ns.doc('get_customer_report')
    @token_required
    def get(self):
        """Get customer report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            limit = int(request.args.get('limit', 20))
            
            report_service = ReportService()
            report = report_service.get_customer_report(start_date.date(), end_date.date(), limit)
            
            return success_response('Customer report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)


@reports_ns.route('/suppliers')
class ReportSuppliers(Resource):
    """Supplier report endpoint"""
    
    @reports_ns.doc('get_supplier_report')
    @token_required
    def get(self):
        """Get supplier report"""
        try:
            from datetime import datetime
            
            start_date = datetime.fromisoformat(request.args.get('start_date'))
            end_date = datetime.fromisoformat(request.args.get('end_date'))
            limit = int(request.args.get('limit', 20))
            
            report_service = ReportService()
            report = report_service.get_supplier_report(start_date.date(), end_date.date(), limit)
            
            return success_response('Supplier report retrieved', report)
        except Exception as e:
            return error_response(str(e), status_code=500)
