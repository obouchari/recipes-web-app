from flask_restx import Resource

from recipes.extensions import api
from recipes.models import User
from recipes.schemas import UserSchema
from recipes.shared.error_handler import error_handler


@api.route("/users/<uuid:user_id>", endpoint="user_detail")
class UserEndpoint(Resource):

    @error_handler()
    def get(self, user_id):
        user = User.find(user_id=user_id)
        user_schema = UserSchema(exclude=["password"])
        return {
            "data": user_schema.dump(user),
        }
