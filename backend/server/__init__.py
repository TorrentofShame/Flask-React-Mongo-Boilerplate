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
from flask_mail import Mail
from server.common.base import FlaskBase
from server.tasks import make_celery

# Flask Config
conf = Config(root_path=os.path.dirname(os.path.realpath(__file__)))
conf.from_object(os.getenv("APP_SETTINGS", "server.config.DevelopmentConfig"))

# Init Extensions
db = MongoEngine()
bcrypt = Bcrypt()
mail = Mail()

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
    ]
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

    # Register Blueprints
    # from server.api.auth import auth_blueprint
    from server.api.users import users_blueprint
    # from server.api.hackers import hackers_blueprint
    
    # app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
    app.register_blueprint(users_blueprint, url_prefix="/api/user")
    # app.register_blueprint(hackers_blueprint, url_prefix="/api/hackers")

    # Register Error Handlers
    # from server.common import exceptions
    # from server.common import error_handlers

    # app.register_error_handler(exceptions.InvalidPayload, error_handlers.handle_exception)
    # app.register_error_handler(exceptions.BusinessException, error_handlers.handle_exception)
    # app.register_error_handler(exceptions.UnauthorizedException, error_handlers.handle_exception)
    # app.register_error_handler(exceptions.ForbiddenException, error_handlers.handle_exception)
    # app.register_error_handler(exceptions.NotFoundException, error_handlers.handle_exception)
    # app.register_error_handler(exceptions.TeapotException, error_handlers.handle_exception)
    # app.register_error_handler(exceptions.ServerErrorException, error_handlers.handle_exception)
    # app.register_error_handler(Exception, error_handlers.handle_general_exception)

    # Setup Celery Task Runner
    celery = make_celery(app)

    return app, celery

app, celery = create_app()

