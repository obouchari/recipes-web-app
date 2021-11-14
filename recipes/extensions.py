from flask import Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_uuid import FlaskUUID
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_talisman import Talisman
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy import MetaData

from recipes.services.spoonacular import Spoonacular

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
uuid = FlaskUUID()

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, version="1.0", title="Recipes API", doc="/doc/")

talisman = Talisman()

jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()
migrate = Migrate()

# Initializing third-party APIs
spoonacular = Spoonacular()
