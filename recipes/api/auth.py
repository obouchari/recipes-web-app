from flask import request, after_this_request
from flask_restx import Resource
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies

from recipes.extensions import api, jwt
from recipes.models import User
from recipes.schemas import UserSchema
from recipes.shared.error_handler import error_handler


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.find(user_id=identity)


@api.route("/login", endpoint="login")
class Login(Resource):

    @error_handler()
    def post(self):
        request_user_schema = UserSchema(only=["email", "password"], load_instance=False)
        result = request_user_schema.load({
            "email": request.authorization.get("username"),
            "password": request.authorization.get("password")
        })
        user = User.authenticate(**result)

        access_token = create_access_token(identity=user)
        user_schema = UserSchema(exclude=["password"])

        @after_this_request
        def set_jwt_cookie(response):
            set_access_cookies(response, access_token)
            return response

        return {
            **user_schema.dump(user)
        }


@api.route("/register", endpoint="register")
class SignUp(Resource):

    @error_handler()
    def post(self):
        request_user_schema = UserSchema(load_instance=False)
        result = request_user_schema.load(request.json)
        user = User.register(**result)
        access_token = create_access_token(identity=user)
        user_schema = UserSchema(exclude=["password"])

        @after_this_request
        def set_jwt_cookie(response):
            set_access_cookies(response, access_token)
            return response

        return {
                   **user_schema.dump(user)
               }, 201


@api.route("/logout", endpoint="logout")
class Logout(Resource):

    @error_handler()
    def post(self):
        @after_this_request
        def unset_jwt_cookie(response):
            unset_jwt_cookies(response)
            return response

        return {
            "message": "success"
        }
