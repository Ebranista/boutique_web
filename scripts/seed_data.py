"""
Seed Initial Data Script

This script seeds the database with initial data including:
- Default roles (Administrator, Manager, Cashier)
- Default permissions
- Default admin user
- Default expense categories
- Default settings
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models.user import User, Role, Permission, RolePermission
from app.models.expense import ExpenseCategory
from app.models.setting import Setting
from app.models.capital import Capital
from datetime import datetime


def seed_roles():
    """Create default roles"""
    roles_data = [
        {'name': 'Administrator', 'description': 'Full system access'},
        {'name': 'Manager', 'description': 'Manage operations and view reports'},
        {'name': 'Cashier', 'description': 'Process sales and view inventory'}
    ]
    
    for role_data in roles_data:
        if not Role.query.filter_by(name=role_data['name']).first():
            role = Role(**role_data)
            db.session.add(role)
            print(f"Created role: {role_data['name']}")
    
    db.session.commit()


def seed_permissions():
    """Create default permissions"""
    permissions_data = [
        # Product permissions
        {'name': 'manage_products', 'module': 'products', 'description': 'Create, update, delete products'},
        # Sales permissions
        {'name': 'manage_sales', 'module': 'sales', 'description': 'Process sales and refunds'},
        # Purchase permissions
        {'name': 'manage_purchases', 'module': 'purchases', 'description': 'Create purchases'},
        # Expense permissions
        {'name': 'manage_expenses', 'module': 'expenses', 'description': 'Create expenses'},
        # User permissions
        {'name': 'manage_users', 'module': 'users', 'description': 'Manage users'},
        # Inventory permissions
        {'name': 'manage_inventory', 'module': 'inventory', 'description': 'Adjust inventory'},
        # Report permissions
        {'name': 'view_reports', 'module': 'reports', 'description': 'View reports'},
        # Settings permissions
        {'name': 'manage_settings', 'module': 'settings', 'description': 'Update settings'},
        # Supplier permissions
        {'name': 'manage_suppliers', 'module': 'suppliers', 'description': 'Manage suppliers'},
        # Customer permissions
        {'name': 'manage_customers', 'module': 'customers', 'description': 'Manage customers'},
    ]
    
    for perm_data in permissions_data:
        if not Permission.query.filter_by(name=perm_data['name']).first():
            permission = Permission(**perm_data)
            db.session.add(permission)
            print(f"Created permission: {perm_data['name']}")
    
    db.session.commit()


def seed_role_permissions():
    """Assign permissions to roles"""
    admin_role = Role.query.filter_by(name='Administrator').first()
    manager_role = Role.query.filter_by(name='Manager').first()
    cashier_role = Role.query.filter_by(name='Cashier').first()
    
    all_permissions = Permission.query.all()
    
    # Administrator gets all permissions
    for permission in all_permissions:
        if not RolePermission.query.filter_by(
            role_id=admin_role.id,
            permission_id=permission.id
        ).first():
            rp = RolePermission(role_id=admin_role.id, permission_id=permission.id)
            db.session.add(rp)
    
    # Manager gets most permissions except user management
    manager_permissions = [p for p in all_permissions if p.name != 'manage_users']
    for permission in manager_permissions:
        if not RolePermission.query.filter_by(
            role_id=manager_role.id,
            permission_id=permission.id
        ).first():
            rp = RolePermission(role_id=manager_role.id, permission_id=permission.id)
            db.session.add(rp)
    
    # Cashier gets limited permissions
    cashier_permission_names = ['manage_sales', 'manage_inventory']
    for permission in all_permissions:
        if permission.name in cashier_permission_names:
            if not RolePermission.query.filter_by(
                role_id=cashier_role.id,
                permission_id=permission.id
            ).first():
                rp = RolePermission(role_id=cashier_role.id, permission_id=permission.id)
                db.session.add(rp)
    
    db.session.commit()
    print("Assigned permissions to roles")


def seed_admin_user():
    """Create default admin user"""
    admin_role = Role.query.filter_by(name='Administrator').first()
    
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@boutique.com',
            first_name='System',
            last_name='Administrator',
            phone='+1234567890',
            is_active=True
        )
        admin.set_password('Admin123!')
        admin.roles.append(admin_role)
        db.session.add(admin)
        db.session.commit()
        print("Created admin user: admin / Admin123!")


def seed_expense_categories():
    """Create default expense categories"""
    categories_data = [
        {'name': 'House Rent', 'description': 'Monthly rent payment', 'is_recurring': True},
        {'name': 'Transportation', 'description': 'Transportation costs', 'is_recurring': False},
        {'name': 'Breakfast', 'description': 'Breakfast expenses', 'is_recurring': False},
        {'name': 'Lunch', 'description': 'Lunch expenses', 'is_recurring': False},
        {'name': 'Electricity', 'description': 'Electricity bills', 'is_recurring': True},
        {'name': 'Water', 'description': 'Water bills', 'is_recurring': True},
        {'name': 'Internet', 'description': 'Internet bills', 'is_recurring': True},
        {'name': 'Guard Salary', 'description': 'Security guard salary', 'is_recurring': True},
        {'name': 'Salary', 'description': 'Employee salaries', 'is_recurring': True},
        {'name': 'Fuel', 'description': 'Fuel expenses', 'is_recurring': False},
        {'name': 'Marketing', 'description': 'Marketing expenses', 'is_recurring': False},
        {'name': 'Miscellaneous', 'description': 'Other expenses', 'is_recurring': False},
    ]
    
    for cat_data in categories_data:
        if not ExpenseCategory.query.filter_by(name=cat_data['name']).first():
            category = ExpenseCategory(**cat_data)
            db.session.add(category)
            print(f"Created expense category: {cat_data['name']}")
    
    db.session.commit()


def seed_settings():
    """Create default settings"""
    if not Setting.query.first():
        settings = Setting(
            shop_name='My Boutique Shop',
            currency='USD',
            currency_symbol='$',
            tax_percentage=18,
            receipt_footer='Thank you for shopping with us!',
            receipt_header='My Boutique Shop',
            low_stock_limit=10,
            dark_mode=False
        )
        db.session.add(settings)
        db.session.commit()
        print("Created default settings")


def seed_capital():
    """Initialize capital"""
    if not Capital.query.filter_by(is_active=True).first():
        capital = Capital(
            beginning_capital=0,
            current_capital=0,
            total_invested=0,
            total_withdrawn=0,
            period_start=datetime.utcnow(),
            is_active=True
        )
        db.session.add(capital)
        db.session.commit()
        print("Initialized capital tracking")


def main():
    """Main seeding function"""
    app = create_app()
    
    with app.app_context():
        print("Starting data seeding...")
        
        seed_roles()
        seed_permissions()
        seed_role_permissions()
        seed_admin_user()
        seed_expense_categories()
        seed_settings()
        seed_capital()
        
        print("\nData seeding completed successfully!")
        print("\nDefault Admin Credentials:")
        print("Username: admin")
        print("Password: Admin123!")
        print("\nPlease change the default password after first login!")


if __name__ == '__main__':
    main()
