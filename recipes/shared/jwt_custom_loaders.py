from marshmallow import ValidationError

from recipes.extensions import jwt
from recipes.shared.error_handler import error_handler
from recipes.shared.error_types import AUTHORIZATION_EXCEPTION


@jwt.unauthorized_loader
@error_handler()
def unauthorized_callback(jwt_payload):
    raise ValidationError({"message": "Authentication Required", **AUTHORIZATION_EXCEPTION})
