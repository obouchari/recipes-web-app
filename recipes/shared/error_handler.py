from functools import wraps
from flask_restx import abort
from marshmallow import ValidationError


def respond_with_error(e):
    abort(e.messages.get("code"), message=e.messages.get("message"), type=e.messages.get("type"))


def error_handler():
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)

            except ValidationError as e:
                respond_with_error(e)
            # except NotFoundException as e:
            # abort(404, error=e.messages)
            # except:
            #     abort(500, msg="Something went wrong.", type="ServerException")

        return wrapper

    return decorator
