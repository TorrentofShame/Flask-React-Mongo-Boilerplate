# -*- coding: utf-8 -*-
"""
    server.__init__
    ~~~~~~~~~~~~~~~

"""
from os import path, getenv

from flask import Config
from flasgger import Swagger
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_mail import Mail
from server.common.base import FlaskBase
from server.tasks import make_celery

import yaml

# Flask Config
conf = Config(root_path=path.dirname(path.realpath(__file__)))
conf.from_object(getenv("APP_SETTINGS", "server.config.DevelopmentConfig"))

# Init Extensions
db = MongoEngine()
bcrypt = Bcrypt()
mail = Mail()
jwt = JWT()

# Load the Schema Definitions
schemapath = path.join(path.abspath(path.dirname(__file__)), "schemas.yml")
schemastream = open(schemapath, "r")
schema = yaml.load(schemastream, Loader=yaml.FullLoader)
schemastream.close()

swagger_template = {
    "swagger": "3.0",
    "info": {
        "title": "Backend API",
        "description": "API for the Backend",
        "contact": {
            "responsibleOrganization": "me",
            "responsibleDeveloper": "me",
            "email": "simon@torrentofshame.com",
            "url": "https://simon.weizman.us"
        },
        "version": "0.0.1"
    },
    "host": "localhost:5000",
    "basePath": "/api",
    "schemes": [
        "http",
        "https"
    ],
    "components": {
        "schemas": schema,
        "securitySchemes": {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization"
            }
        }
    }
}
swagger = Swagger(template=swagger_template)


def create_app():
    """Initialize the App"""
    app = FlaskBase(__name__)

    from server.common.utils import authenticate, identity

    # Setup Extensions
    db.init_app(app)
    swagger.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    jwt.authentication_callback = authenticate
    jwt.identity_callback = identity
    jwt.init_app(app)

    # Register Blueprints
    from server.api.auth import auth_blueprint
    from server.api.users import users_blueprint
    from server.api.hackers import hackers_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
    app.register_blueprint(users_blueprint, url_prefix="/api/users")
    app.register_blueprint(hackers_blueprint, url_prefix="/api/hackers")


    # Setup Celery Task Runner
    celery = make_celery(app)

    return app, celery

app, celery = create_app()

