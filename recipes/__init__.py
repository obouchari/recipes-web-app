from flask import Flask, send_from_directory

import recipes.api
import recipes.shared.jwt_custom_loaders
from recipes.config import configurations
from recipes.extensions import (db, uuid, jwt, talisman, blueprint, bcrypt, ma, migrate, spoonacular)


def create_app(environment_name="dev"):
    app = Flask(__name__, static_folder="../client/dist")
    app.config.from_object(configurations[environment_name])
    db.init_app(app)
    uuid.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    talisman.init_app(app, content_security_policy={
        "default-src": ["'self'", "*"],
        "script-src": ["'self'", "'unsafe-inline'"],
        "style-src": ["'self'", "'unsafe-inline'"],
        "img-src": "*"
    })

    app.register_blueprint(blueprint)

    spoonacular.init_app(app)

    @app.route("/assets/<path:path>")
    def assets(path):
        return send_from_directory("../client/dist/assets", path)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def base(path):
        return send_from_directory("../client/dist", "index.html")

    return app
