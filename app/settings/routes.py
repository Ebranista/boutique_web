"""
Settings Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.setting_service import SettingService
from app.schemas.setting import SettingUpdateSchema
from app.utils.response import success_response, error_response
from app.middleware.auth import token_required, admin_required

# Create namespace
settings_ns = Namespace('settings', description='Settings operations')

settings_update_model = settings_ns.model('SettingsUpdate', {
    'shop_name': fields.String,
    'logo': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'email': fields.String,
    'currency': fields.String,
    'currency_symbol': fields.String,
    'tax_percentage': fields.Integer,
    'receipt_footer': fields.String,
    'receipt_header': fields.String,
    'low_stock_limit': fields.Integer,
    'dark_mode': fields.Boolean,
    'tin_number': fields.String
})


@settings_ns.route('/')
class Settings(Resource):
    """Settings endpoint"""
    
    @settings_ns.doc('get_settings')
    @token_required
    def get(self):
        """Get settings"""
        try:
            setting_service = SettingService()
            settings = setting_service.get_settings()
            if settings:
                return success_response('Settings retrieved', settings.to_dict())
            return error_response('Settings not found', status_code=404)
        except Exception as e:
            return error_response(str(e), status_code=500)
    
    @settings_ns.doc('update_settings')
    @admin_required
    @settings_ns.expect(settings_update_model)
    def put(self):
        """Update settings"""
        try:
            data = request.get_json()
            schema = SettingUpdateSchema()
            errors = schema.validate(data)
            
            if errors:
                return error_response('Validation failed', errors, 400)
            
            setting_service = SettingService()
            settings = setting_service.update_settings(data)
            if settings:
                return success_response('Settings updated successfully', settings.to_dict())
            return error_response('Settings update failed', status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@settings_ns.route('/initialize')
class InitializeSettings(Resource):
    """Initialize settings endpoint"""
    
    @settings_ns.doc('initialize_settings')
    @admin_required
    def post(self):
        """Initialize default settings"""
        try:
            setting_service = SettingService()
            settings = setting_service.initialize_default_settings()
            return success_response('Settings initialized successfully', settings.to_dict())
        except Exception as e:
            return error_response(str(e), status_code=500)
