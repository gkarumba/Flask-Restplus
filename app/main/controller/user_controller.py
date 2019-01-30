from flask import request
from flask_restplus import Resource

from app.main.util.dto import UserDto
from app.main.service.user_service import save_new_user,get_a_user,get_all_users

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_all_users()
        
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return save_new_user(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The User Identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user