"""
Capital Routes
"""
from flask import request
from flask_restx import Namespace, Resource, fields
from decimal import Decimal
from app.services.capital_service import CapitalService
from app.schemas.capital import CapitalSchema, CapitalInvestmentSchema, CapitalWithdrawalSchema
from app.utils.response import success_response, error_response, paginated_response
from app.middleware.auth import token_required, permission_required

capital_ns = Namespace('capital', description='Capital operations')

capital_investment_model = capital_ns.model('CapitalInvestment', {
    'amount': fields.Float(required=True),
    'notes': fields.String
})

capital_withdrawal_model = capital_ns.model('CapitalWithdrawal', {
    'amount': fields.Float(required=True),
    'notes': fields.String
})


@capital_ns.route('/')
class CapitalOverview(Resource):
    """Capital overview endpoint"""

    @capital_ns.doc('get_current_capital')
    @token_required
    def get(self):
        """Get current active capital"""
        try:
            capital_service = CapitalService()
            capital = capital_service.get_current_capital()
            if capital:
                schema = CapitalSchema()
                return success_response('Current capital retrieved', schema.dump(capital))
            return success_response('No active capital period found', None)
        except Exception as e:
            return error_response(str(e), status_code=500)


@capital_ns.route('/history')
class CapitalHistory(Resource):
    """Capital history endpoint"""

    @capital_ns.doc('get_capital_history')
    @token_required
    def get(self):
        """Get capital history"""
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))

            capital_service = CapitalService()
            capital_records, total = capital_service.get_capital_history(page, per_page)
            schema = CapitalSchema(many=True)
            return paginated_response(
                schema.dump(capital_records),
                total,
                page,
                per_page,
                message='Capital history retrieved'
            )
        except Exception as e:
            return error_response(str(e), status_code=500)


@capital_ns.route('/invest')
class CapitalInvest(Resource):
    """Add capital investment endpoint"""

    @capital_ns.doc('add_capital_investment')
    @permission_required('manage_expenses')
    @capital_ns.expect(capital_investment_model)
    def post(self):
        """Add capital investment"""
        try:
            data = request.get_json()
            schema = CapitalInvestmentSchema()
            errors = schema.validate(data)
            if errors:
                return error_response('Validation failed', errors, 400)

            capital_service = CapitalService()
            capital = capital_service.add_capital(
                amount=Decimal(str(data['amount'])),
                notes=data.get('notes')
            )
            schema = CapitalSchema()
            return success_response('Capital investment added', schema.dump(capital))
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)


@capital_ns.route('/withdraw')
class CapitalWithdraw(Resource):
    """Capital withdrawal endpoint"""

    @capital_ns.doc('reduce_capital')
    @permission_required('manage_expenses')
    @capital_ns.expect(capital_withdrawal_model)
    def post(self):
        """Withdraw capital"""
        try:
            data = request.get_json()
            schema = CapitalWithdrawalSchema()
            errors = schema.validate(data)
            if errors:
                return error_response('Validation failed', errors, 400)

            capital_service = CapitalService()
            capital = capital_service.reduce_capital(
                amount=Decimal(str(data['amount'])),
                notes=data.get('notes')
            )
            schema = CapitalSchema()
            return success_response('Capital withdrawn', schema.dump(capital))
        except ValueError as e:
            return error_response(str(e), status_code=400)
        except Exception as e:
            return error_response(str(e), status_code=500)
