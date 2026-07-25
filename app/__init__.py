"""
Flask Application Factory
"""
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from .utils.response import JSONEncoder

# Load environment variables
load_dotenv()

# Import extensions
from .extensions import db, migrate, jwt, cors


def create_app(config_name=None):
    """
    Application Factory Pattern
    
    Args:
        config_name: Configuration environment (development, testing, production)
    
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    from .config import config
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    initialize_extensions(app)
    
    # Register blueprints
    register_blueprints(app)
    
    # Setup logging
    setup_logging(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Register middleware
    register_middleware(app)
    
    return app


def initialize_extensions(app: Flask) -> None:
    """Initialize Flask extensions"""
    # Database
    db.init_app(app)
    
    # Migrations
    migrate.init_app(app, db)
    
    # JWT
    jwt.init_app(app)
    
    # CORS
    cors.init_app(app, origins=app.config['CORS_ORIGINS'])


def register_blueprints(app: Flask) -> None:
    """Register Flask blueprints"""
    api_v1_prefix = '/api/v1'
    
    # Create API instance
    api = Api(
        app,
        version='1.0',
        title='Boutique Shop Management API',
        description='A comprehensive API for boutique shop management',
        doc=f'{api_v1_prefix}/swagger/',
        prefix=api_v1_prefix
    )
    
    # Configure Flask-RESTX to use custom JSON encoder
    api.json_encoder = JSONEncoder
    
    # Register namespaces
    from .auth.routes import auth_ns
    from .users.routes import users_ns
    from .dashboard.routes import dashboard_ns
    from .products.routes import products_ns
    from .categories.routes import categories_ns
    from .brands.routes import brands_ns
    from .inventory.routes import inventory_ns
    from .suppliers.routes import suppliers_ns
    from .customers.routes import customers_ns
    from .purchases.routes import purchases_ns
    from .sales.routes import sales_ns
    from .expenses.routes import expenses_ns
    from .reports.routes import reports_ns
    from .notifications.routes import notifications_ns
    from .settings.routes import settings_ns
    from .audit.routes import audit_ns
    from .roles.routes import roles_ns
    from .permissions.routes import permissions_ns
    from .capital.routes import capital_ns
    
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(users_ns, path='/users')
    api.add_namespace(dashboard_ns, path='/dashboard')
    api.add_namespace(products_ns, path='/products')
    api.add_namespace(categories_ns, path='/categories')
    api.add_namespace(brands_ns, path='/brands')
    api.add_namespace(inventory_ns, path='/inventory')
    api.add_namespace(suppliers_ns, path='/suppliers')
    api.add_namespace(customers_ns, path='/customers')
    api.add_namespace(purchases_ns, path='/purchases')
    api.add_namespace(sales_ns, path='/sales')
    api.add_namespace(expenses_ns, path='/expenses')
    api.add_namespace(reports_ns, path='/reports')
    api.add_namespace(notifications_ns, path='/notifications')
    api.add_namespace(settings_ns, path='/settings')
    api.add_namespace(roles_ns, path='/roles')
    api.add_namespace(permissions_ns, path='/permissions')
    api.add_namespace(capital_ns, path='/capital')
    api.add_namespace(audit_ns, path='/audit')


def setup_logging(app: Flask) -> None:
    """Setup application logging"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Create formatters
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s %(name)s %(message)s'
    )
    
    # File handler
    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=10485760,
        backupCount=10
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG if app.debug else logging.INFO)
    
    # Apply to app logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.DEBUG if app.debug else logging.INFO)
    
    app.logger.info('Boutique Shop Management System initialized')


def register_error_handlers(app: Flask) -> None:
    """Register global error handlers"""
    from flask import jsonify
    from werkzeug.exceptions import HTTPException
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        """Handle HTTP exceptions"""
        response = {
            'success': False,
            'message': e.description,
            'error': e.name
        }
        return jsonify(response), e.code
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        """Handle unhandled exceptions"""
        app.logger.error(f'Unhandled exception: {str(e)}', exc_info=True)
        response = {
            'success': False,
            'message': 'Internal server error',
            'error': str(e) if app.debug else 'An unexpected error occurred'
        }
        return jsonify(response), 500


def register_middleware(app: Flask) -> None:
    """Register application middleware"""
    @app.before_request
    def before_request():
        """Execute before each request"""
        from flask import request
        app.logger.debug(f'{request.method} {request.path}')
    
    @app.after_request
    def after_request(response):
        """Execute after each request"""
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        return response
