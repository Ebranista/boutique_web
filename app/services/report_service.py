"""
Report Service
"""
from typing import Dict, Any, List
from decimal import Decimal
from datetime import datetime, date
from sqlalchemy import func, extract
from app.models.sale import Sale, SaleItem
from app.models.purchase import Purchase
from app.models.expense import Expense
from app.models.product import Product
from app.models.customer import Customer
from app.models.supplier import Supplier
from app.extensions import db


class ReportService:
    """Report service for generating various reports"""
    
    def get_sales_report(
        self,
        start_date: date,
        end_date: date,
        page: int = 1,
        per_page: int = 20
    ) -> Dict[str, Any]:
        """
        Generate sales report
        
        Args:
            start_date: Start date
            end_date: End date
            page: Page number
            per_page: Items per page
            
        Returns:
            Sales report data
        """
        query = Sale.query.filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        )
        
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        
        # Calculate totals
        total_sales = db.session.query(func.sum(Sale.total)).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        total_profit = db.session.query(func.sum(Sale.total_profit)).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        total_items = db.session.query(func.sum(SaleItem.quantity)).join(
            Sale, SaleItem.sale_id == Sale.id
        ).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or 0
        
        return {
            'sales': [sale.to_dict() for sale in pagination.items],
            'total_sales': float(total_sales),
            'total_profit': float(total_profit),
            'total_items': total_items,
            'total_count': pagination.total,
            'page': page,
            'per_page': per_page
        }
    
    def get_purchase_report(
        self,
        start_date: date,
        end_date: date,
        page: int = 1,
        per_page: int = 20
    ) -> Dict[str, Any]:
        """
        Generate purchase report
        
        Args:
            start_date: Start date
            end_date: End date
            page: Page number
            per_page: Items per page
            
        Returns:
            Purchase report data
        """
        query = Purchase.query.filter(
            Purchase.purchase_date >= start_date,
            Purchase.purchase_date <= end_date,
            Purchase.is_deleted == False,
            Purchase.status == 'completed'
        )
        
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        
        # Calculate totals
        total_purchases = db.session.query(func.sum(Purchase.total)).filter(
            Purchase.purchase_date >= start_date,
            Purchase.purchase_date <= end_date,
            Purchase.is_deleted == False,
            Purchase.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        return {
            'purchases': [purchase.to_dict() for purchase in pagination.items],
            'total_purchases': float(total_purchases),
            'total_count': pagination.total,
            'page': page,
            'per_page': per_page
        }
    
    def get_expense_report(
        self,
        start_date: date,
        end_date: date,
        page: int = 1,
        per_page: int = 20
    ) -> Dict[str, Any]:
        """
        Generate expense report
        
        Args:
            start_date: Start date
            end_date: End date
            page: Page number
            per_page: Items per page
            
        Returns:
            Expense report data
        """
        query = Expense.query.filter(
            Expense.expense_date >= start_date,
            Expense.expense_date <= end_date,
            Expense.is_deleted == False
        )
        
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        
        # Calculate totals
        total_expenses = db.session.query(func.sum(Expense.amount)).filter(
            Expense.expense_date >= start_date,
            Expense.expense_date <= end_date,
            Expense.is_deleted == False
        ).scalar() or Decimal('0.00')
        
        # Group by category
        category_breakdown = db.session.query(
            Expense.category_id,
            func.sum(Expense.amount).label('total')
        ).filter(
            Expense.expense_date >= start_date,
            Expense.expense_date <= end_date,
            Expense.is_deleted == False
        ).group_by(Expense.category_id).all()
        
        return {
            'expenses': [expense.to_dict() for expense in pagination.items],
            'total_expenses': float(total_expenses),
            'category_breakdown': [
                {'category_id': cat[0], 'total': float(cat[1])}
                for cat in category_breakdown
            ],
            'total_count': pagination.total,
            'page': page,
            'per_page': per_page
        }
    
    def get_inventory_report(self, page: int = 1, per_page: int = 20) -> Dict[str, Any]:
        """
        Generate inventory report
        
        Args:
            page: Page number
            per_page: Items per page
            
        Returns:
            Inventory report data
        """
        from app.models.inventory import Inventory
        
        query = Inventory.query.filter_by(is_deleted=False)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        
        # Calculate totals
        total_value = db.session.query(func.sum(Inventory.total_value)).filter(
            Inventory.is_deleted == False
        ).scalar() or Decimal('0.00')
        
        total_quantity = db.session.query(func.sum(Inventory.quantity)).filter(
            Inventory.is_deleted == False
        ).scalar() or 0
        
        return {
            'inventory': [inv.to_dict() for inv in pagination.items],
            'total_value': float(total_value),
            'total_quantity': total_quantity,
            'total_count': pagination.total,
            'page': page,
            'per_page': per_page
        }
    
    def get_profit_report(
        self,
        start_date: date,
        end_date: date
    ) -> Dict[str, Any]:
        """
        Generate profit report
        
        Args:
            start_date: Start date
            end_date: End date
            
        Returns:
            Profit report data
        """
        # Total revenue
        revenue = db.session.query(func.sum(Sale.total)).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        # Total cost
        cost = db.session.query(func.sum(Sale.total_cost)).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).scalar() or Decimal('0.00')
        
        # Total expenses
        expenses = db.session.query(func.sum(Expense.amount)).filter(
            Expense.expense_date >= start_date,
            Expense.expense_date <= end_date,
            Expense.is_deleted == False
        ).scalar() or Decimal('0.00')
        
        # Gross profit
        gross_profit = revenue - cost
        
        # Net profit
        net_profit = gross_profit - expenses
        
        # Profit margin
        profit_margin = (net_profit / revenue * 100) if revenue > 0 else 0
        
        return {
            'revenue': float(revenue),
            'cost': float(cost),
            'expenses': float(expenses),
            'gross_profit': float(gross_profit),
            'net_profit': float(net_profit),
            'profit_margin': float(profit_margin)
        }
    
    def get_product_profit_report(
        self,
        start_date: date,
        end_date: date,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Generate product profit report
        
        Args:
            start_date: Start date
            end_date: End date
            limit: Number of products to return
            
        Returns:
            Product profit data
        """
        results = db.session.query(
            Product.id,
            Product.name,
            func.sum(SaleItem.quantity).label('total_quantity'),
            func.sum(SaleItem.subtotal).label('total_revenue'),
            func.sum(SaleItem.cost).label('total_cost'),
            func.sum(SaleItem.profit).label('total_profit')
        ).join(
            SaleItem, Product.id == SaleItem.product_id
        ).join(
            Sale, SaleItem.sale_id == Sale.id
        ).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).group_by(
            Product.id, Product.name
        ).order_by(
            func.sum(SaleItem.profit).desc()
        ).limit(limit).all()
        
        return [
            {
                'product_id': result[0],
                'product_name': result[1],
                'total_quantity': result[2],
                'total_revenue': float(result[3]),
                'total_cost': float(result[4]),
                'total_profit': float(result[5])
            }
            for result in results
        ]
    
    def get_customer_report(
        self,
        start_date: date,
        end_date: date,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Generate customer report
        
        Args:
            start_date: Start date
            end_date: End date
            limit: Number of customers to return
            
        Returns:
            Customer data
        """
        results = db.session.query(
            Customer.id,
            Customer.name,
            func.count(Sale.id).label('total_purchases'),
            func.sum(Sale.total).label('total_spent')
        ).join(
            Sale, Customer.id == Sale.customer_id
        ).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date,
            Sale.is_deleted == False,
            Sale.status == 'completed'
        ).group_by(
            Customer.id, Customer.name
        ).order_by(
            func.sum(Sale.total).desc()
        ).limit(limit).all()
        
        return [
            {
                'customer_id': result[0],
                'customer_name': result[1],
                'total_purchases': result[2],
                'total_spent': float(result[3])
            }
            for result in results
        ]
    
    def get_supplier_report(
        self,
        start_date: date,
        end_date: date,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Generate supplier report
        
        Args:
            start_date: Start date
            end_date: End date
            limit: Number of suppliers to return
            
        Returns:
            Supplier data
        """
        results = db.session.query(
            Supplier.id,
            Supplier.name,
            func.count(Purchase.id).label('total_purchases'),
            func.sum(Purchase.total).label('total_amount')
        ).join(
            Purchase, Supplier.id == Purchase.supplier_id
        ).filter(
            Purchase.purchase_date >= start_date,
            Purchase.purchase_date <= end_date,
            Purchase.is_deleted == False,
            Purchase.status == 'completed'
        ).group_by(
            Supplier.id, Supplier.name
        ).order_by(
            func.sum(Purchase.total).desc()
        ).limit(limit).all()
        
        return [
            {
                'supplier_id': result[0],
                'supplier_name': result[1],
                'total_purchases': result[2],
                'total_amount': float(result[3])
            }
            for result in results
        ]
