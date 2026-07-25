"""
Dashboard Service
"""
from typing import Dict, Any
from decimal import Decimal
from datetime import datetime, date
from sqlalchemy import func, extract
from app.models.sale import Sale
from app.models.purchase import Purchase
from app.models.expense import Expense
from app.models.product import Product
from app.models.customer import Customer
from app.models.supplier import Supplier
from app.models.capital import Capital
from app.extensions import db


class DashboardService:
    """Dashboard service for analytics and statistics"""
    
    def get_today_stats(self) -> Dict[str, Any]:
        """Get today's statistics"""
        today = date.today()
        
        # Today's sales
        today_sales = db.session.query(func.sum(Sale.total)).filter(
            func.date(Sale.sale_date) == today,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        # Today's profit
        today_profit = db.session.query(func.sum(Sale.total_profit)).filter(
            func.date(Sale.sale_date) == today,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        # Today's expenses
        today_expenses = db.session.query(func.sum(Expense.amount)).filter(
            func.date(Expense.expense_date) == today,
            Expense.is_deleted == False
        ).scalar() or Decimal('0.00')
        
        return {
            'today_sales': float(today_sales),
            'today_profit': float(today_profit),
            'today_expenses': float(today_expenses)
        }
    
    def get_monthly_stats(self) -> Dict[str, Any]:
        """Get monthly statistics"""
        now = datetime.utcnow()
        year = now.year
        month = now.month
        
        # Monthly sales
        monthly_sales = db.session.query(func.sum(Sale.total)).filter(
            extract('year', Sale.sale_date) == year,
            extract('month', Sale.sale_date) == month,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        # Monthly profit
        monthly_profit = db.session.query(func.sum(Sale.total_profit)).filter(
            extract('year', Sale.sale_date) == year,
            extract('month', Sale.sale_date) == month,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        # Monthly expenses
        monthly_expenses = db.session.query(func.sum(Expense.amount)).filter(
            extract('year', Expense.expense_date) == year,
            extract('month', Expense.expense_date) == month,
            Expense.is_deleted == False
        ).scalar() or Decimal('0.00')
        
        return {
            'monthly_sales': float(monthly_sales),
            'monthly_profit': float(monthly_profit),
            'monthly_expenses': float(monthly_expenses)
        }
    
    def get_inventory_stats(self) -> Dict[str, Any]:
        """Get inventory statistics"""
        # Total products
        total_products = Product.query.filter_by(is_deleted=False).count()
        
        # Low stock count
        low_stock_count = db.session.query(func.count(Product.id)).filter(
            Product.quantity <= Product.minimum_stock,
            Product.is_deleted == False
        ).scalar() or 0
        
        # Out of stock count
        out_of_stock_count = Product.query.filter_by(
            quantity=0,
            is_deleted=False
        ).count()
        
        return {
            'total_products': total_products,
            'low_stock_count': low_stock_count,
            'out_of_stock_count': out_of_stock_count
        }
    
    def get_entity_counts(self) -> Dict[str, Any]:
        """Get counts of various entities"""
        return {
            'total_customers': Customer.query.filter_by(is_deleted=False).count(),
            'total_suppliers': Supplier.query.filter_by(is_deleted=False).count(),
            'total_products': Product.query.filter_by(is_deleted=False).count(),
            'total_expenses': Expense.query.filter_by(is_deleted=False).count()
        }
    
    def get_current_capital(self) -> Dict[str, Any]:
        """Get current capital"""
        capital = Capital.query.filter_by(is_active=True).first()
        
        if capital:
            return {
                'current_capital': float(capital.current_capital),
                'capital_growth': float(capital.capital_growth)
            }
        
        return {
            'current_capital': 0.0,
            'capital_growth': 0.0
        }
    
    def get_top_selling_products(self, limit: int = 10) -> list:
        """Get top selling products"""
        from app.models.sale import SaleItem
        
        results = db.session.query(
            Product.name,
            func.sum(SaleItem.quantity).label('total_quantity'),
            func.sum(SaleItem.subtotal).label('total_revenue')
        ).join(
            SaleItem, Product.id == SaleItem.product_id
        ).join(
            Sale, SaleItem.sale_id == Sale.id
        ).filter(
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).group_by(
            Product.id, Product.name
        ).order_by(
            func.sum(SaleItem.quantity).desc()
        ).limit(limit).all()
        
        return [
            {
                'name': result[0],
                'total_quantity': result[1],
                'total_revenue': float(result[2])
            }
            for result in results
        ]
    
    def get_recent_sales(self, limit: int = 10) -> list:
        """Get recent sales"""
        sales = Sale.query.filter_by(
            is_deleted=False
        ).order_by(
            Sale.sale_date.desc()
        ).limit(limit).all()
        
        return [
            {
                'invoice_number': sale.invoice_number,
                'total': float(sale.total),
                'sale_date': sale.sale_date.isoformat(),
                'customer_name': sale.customer.name if sale.customer else None
            }
            for sale in sales
        ]
    
    def get_recent_expenses(self, limit: int = 10) -> list:
        """Get recent expenses"""
        expenses = Expense.query.filter_by(
            is_deleted=False
        ).order_by(
            Expense.expense_date.desc()
        ).limit(limit).all()
        
        return [
            {
                'name': expense.name,
                'amount': float(expense.amount),
                'expense_date': expense.expense_date.isoformat(),
                'category_name': expense.category.name if expense.category else None
            }
            for expense in expenses
        ]
    
    def get_monthly_chart_data(self, months: int = 12) -> Dict[str, Any]:
        """Get monthly chart data for sales, expenses, and profit"""
        from dateutil.relativedelta import relativedelta
        
        sales_data = []
        expenses_data = []
        profit_data = []
        labels = []
        
        for i in range(months):
            date = datetime.utcnow() - relativedelta(months=months - i - 1)
            year = date.year
            month = date.month
            
            # Sales
            sales = db.session.query(func.sum(Sale.total)).filter(
                extract('year', Sale.sale_date) == year,
                extract('month', Sale.sale_date) == month,
                Sale.is_deleted == False,
                Sale.status == 'completed'
            ).scalar() or Decimal('0.00')
            
            # Expenses
            expenses = db.session.query(func.sum(Expense.amount)).filter(
                extract('year', Expense.expense_date) == year,
                extract('month', Expense.expense_date) == month,
                Expense.is_deleted == False
            ).scalar() or Decimal('0.00')
            
            # Profit
            profit = sales - expenses
            
            sales_data.append(float(sales))
            expenses_data.append(float(expenses))
            profit_data.append(float(profit))
            labels.append(date.strftime('%b %Y'))
        
        return {
            'sales': sales_data,
            'expenses': expenses_data,
            'profit': profit_data,
            'labels': labels
        }
    
    def get_dashboard_summary(self) -> Dict[str, Any]:
        """Get complete dashboard summary"""
        return {
            'today_stats': self.get_today_stats(),
            'monthly_stats': self.get_monthly_stats(),
            'inventory_stats': self.get_inventory_stats(),
            'entity_counts': self.get_entity_counts(),
            'current_capital': self.get_current_capital(),
            'top_selling_products': self.get_top_selling_products(),
            'recent_sales': self.get_recent_sales(),
            'recent_expenses': self.get_recent_expenses(),
            'monthly_chart_data': self.get_monthly_chart_data()
        }
