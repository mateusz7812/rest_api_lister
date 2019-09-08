import logging

from flask import request
from flask_restplus import Resource
from rest_api_lister.api.blog.business import create_list, update_list, delete_list
from rest_api_lister.api.blog.serializers import lister_list, page_of_lists
from rest_api_lister.api.blog.parsers import pagination_arguments
from rest_api_lister.api.restplus import api
from rest_api_lister.database.models import List

log = logging.getLogger(__name__)

ns = api.namespace('lists', description='Operations related to lists')


@ns.route('/')
class ListsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_lists)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        lists_query = List.query
        lists_page = lists_query.paginate(page, per_page, error_out=False)

        return lists_page

    @api.expect(lister_list)
    def post(self):
        create_list(request.json)
        return None, 201


@ns.route('/<int:list_id>')
@api.response(404, 'List not found.')
class ListItem(Resource):

    @api.marshal_with(lister_list)
    def get(self, list_id):
        return List.query.filter(List.id == list_id).one()

    @api.expect(lister_list)
    @api.response(204, 'List successfully updated.')
    def put(self, list_id):
        data = request.json
        update_list(list_id, data)
        return None, 204

    @api.response(204, 'List successfully deleted.')
    def delete(self, list_id):
        delete_list(list_id)
        return None, 204
