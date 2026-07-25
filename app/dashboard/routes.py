"""
Dashboard Routes
"""
from flask import request
from flask_restx import Namespace, Resource
from app.services.dashboard_service import DashboardService
from app.utils.response import success_response, error_response
from app.middleware.auth import token_required

# Create namespace
dashboard_ns = Namespace('dashboard', description='Dashboard operations')


@dashboard_ns.route('/summary')
class DashboardSummary(Resource):
    """Dashboard summary endpoint"""
    
    @dashboard_ns.doc('get_dashboard_summary')
    @token_required
    def get(self):
        """Get complete dashboard summary"""
        try:
            dashboard_service = DashboardService()
            summary = dashboard_service.get_dashboard_summary()
            return success_response('Dashboard summary retrieved', summary)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/today-stats')
class TodayStats(Resource):
    """Today's statistics endpoint"""
    
    @dashboard_ns.doc('get_today_stats')
    @token_required
    def get(self):
        """Get today's statistics"""
        try:
            dashboard_service = DashboardService()
            stats = dashboard_service.get_today_stats()
            return success_response('Today\'s statistics retrieved', stats)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/monthly-stats')
class MonthlyStats(Resource):
    """Monthly statistics endpoint"""
    
    @dashboard_ns.doc('get_monthly_stats')
    @token_required
    def get(self):
        """Get monthly statistics"""
        try:
            dashboard_service = DashboardService()
            stats = dashboard_service.get_monthly_stats()
            return success_response('Monthly statistics retrieved', stats)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/inventory-stats')
class InventoryStats(Resource):
    """Inventory statistics endpoint"""
    
    @dashboard_ns.doc('get_inventory_stats')
    @token_required
    def get(self):
        """Get inventory statistics"""
        try:
            dashboard_service = DashboardService()
            stats = dashboard_service.get_inventory_stats()
            return success_response('Inventory statistics retrieved', stats)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/entity-counts')
class EntityCounts(Resource):
    """Entity counts endpoint"""
    
    @dashboard_ns.doc('get_entity_counts')
    @token_required
    def get(self):
        """Get counts of various entities"""
        try:
            dashboard_service = DashboardService()
            counts = dashboard_service.get_entity_counts()
            return success_response('Entity counts retrieved', counts)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/capital')
class CurrentCapital(Resource):
    """Current capital endpoint"""
    
    @dashboard_ns.doc('get_current_capital')
    @token_required
    def get(self):
        """Get current capital"""
        try:
            dashboard_service = DashboardService()
            capital = dashboard_service.get_current_capital()
            return success_response('Current capital retrieved', capital)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/top-products')
class TopSellingProducts(Resource):
    """Top selling products endpoint"""
    
    @dashboard_ns.doc('get_top_selling_products')
    @token_required
    def get(self):
        """Get top selling products"""
        try:
            limit = int(request.args.get('limit', 10))
            dashboard_service = DashboardService()
            products = dashboard_service.get_top_selling_products(limit)
            return success_response('Top selling products retrieved', products)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/recent-sales')
class RecentSales(Resource):
    """Recent sales endpoint"""
    
    @dashboard_ns.doc('get_recent_sales')
    @token_required
    def get(self):
        """Get recent sales"""
        try:
            limit = int(request.args.get('limit', 10))
            dashboard_service = DashboardService()
            sales = dashboard_service.get_recent_sales(limit)
            return success_response('Recent sales retrieved', sales)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/recent-expenses')
class RecentExpenses(Resource):
    """Recent expenses endpoint"""
    
    @dashboard_ns.doc('get_recent_expenses')
    @token_required
    def get(self):
        """Get recent expenses"""
        try:
            limit = int(request.args.get('limit', 10))
            dashboard_service = DashboardService()
            expenses = dashboard_service.get_recent_expenses(limit)
            return success_response('Recent expenses retrieved', expenses)
        except Exception as e:
            return error_response(str(e), status_code=500)


@dashboard_ns.route('/monthly-chart')
class MonthlyChart(Resource):
    """Monthly chart data endpoint"""
    
    @dashboard_ns.doc('get_monthly_chart_data')
    @token_required
    def get(self):
        """Get monthly chart data"""
        try:
            months = int(request.args.get('months', 12))
            dashboard_service = DashboardService()
            data = dashboard_service.get_monthly_chart_data(months)
            return success_response('Monthly chart data retrieved', data)
        except Exception as e:
            return error_response(str(e), status_code=500)
