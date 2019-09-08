from flask_restplus import fields
from rest_api_lister.api.restplus import api

lister_list = api.model('List', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a list'),
    'title': fields.String(required=True, description='List title'),
    'body': fields.String(required=True, description='List content'),
    'pub_date': fields.DateTime,
    'account_id': fields.Integer(attribute='account.id'),
    'account': fields.String(attribute='account.nick'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_lists = api.inherit('Page of lists', pagination, {
    'items': fields.List(fields.Nested(lister_list))
})

account = api.model('Account', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an account'),
    'nick': fields.String(required=True, description='Account name'),
})

account_extended = api.inherit('Account with lists and contacts', account, {
    'lists': fields.List(fields.Nested(lister_list)),
    'contacts': fields.String(required=True)
})

