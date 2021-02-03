# -*- coding: utf-8 -*-
"""
    server.__init__
    ~~~~~~~~~~~~~~~

"""
import os

from flask import Config
from flasgger import Swagger
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_mail import Mail
from server.common.base import FlaskBase
from server.tasks import make_celery
from server.common.utils import authenticate, identity
import yaml

# Flask Config
conf = Config(root_path=os.path.dirname(os.path.realpath(__file__)))
conf.from_object(os.getenv("APP_SETTINGS", "server.config.DevelopmentConfig"))

# Init Extensions
db = MongoEngine()
bcrypt = Bcrypt()
mail = Mail()
jwt = JWT()

ymlstream = open("/home/backend/app/server/schemas.yml", "r")
schema = yaml.load(ymlstream)
ymlstream.close()

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
        "schemas": schema
    }
}
swagger = Swagger(template=swagger_template)


def create_app():
    """Initialize the App"""
    app = FlaskBase(__name__)

    # Setup Extensions
    db.init_app(app)
    swagger.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    jwt.init_app(app, authenticate, identity)

    # Register Blueprints
    from server.api.auth import auth_blueprint
    from server.api.users import users_blueprint
    from server.api.hackers import hackers_blueprint
    
    app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
    app.register_blueprint(users_blueprint, url_prefix="/api/user")
    app.register_blueprint(hackers_blueprint, url_prefix="/api/hackers")


    # Setup Celery Task Runner
    celery = make_celery(app)

    return app, celery

app, celery = create_app()

