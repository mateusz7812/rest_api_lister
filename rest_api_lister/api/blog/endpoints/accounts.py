import logging

from flask import request
from flask_restplus import Resource
from rest_api_lister.api.blog.business import create_account, delete_account, update_account
from rest_api_lister.api.blog.serializers import account, account_extended
from rest_api_lister.api.restplus import api
from rest_api_lister.database.models import Account

log = logging.getLogger(__name__)

ns = api.namespace('accounts', description='Operations related to accounts')


@ns.route('/')
class AccountsCollection(Resource):

    @api.marshal_list_with(account)
    def get(self):
        accounts = Account.query.all()
        return accounts

    @api.response(201, 'Account successfully created.')
    @api.expect(account)
    def post(self):
        data = request.json
        create_account(data)
        return None, 201


@ns.route('/<int:account_id>')
@api.response(404, 'Account not found.')
class AccountsItem(Resource):

    @api.marshal_with(account_extended)
    def get(self, account_id):
        return Account.query.filter(Account.id == account_id).one()

    @api.expect(account)
    @api.response(204, 'Account successfully updated.')
    def put(self, account_id):
        data = request.json
        update_account(account_id, data)
        return None, 204

    @api.response(204, 'Account successfully deleted.')
    def delete(self, account_id):
        delete_account(account_id)
        return None, 204
