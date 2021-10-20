from flask import Flask

from recipes.blueprints.users import users
from recipes.blueprints.recipes import recipes
from recipes.config import configurations
from recipes.extensions import db, uuid


def create_app(environment_name="dev"):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    db.init_app(app)
    uuid.init_app(app)

    app.register_blueprint(users, url_prefix="/users")
    app.register_blueprint(recipes, url_prefix="/recipes")

    return app
