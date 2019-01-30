from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from app.main.util.dto import AuhDto

api = AuhDto.api
user_auth = AuhDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.login_user(data=post_data)

@api.route('/logout')
class LogoutApi(Resource):
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)