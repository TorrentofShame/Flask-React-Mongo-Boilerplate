# -*- coding: utf-8 -*-
"""
    server.config
    ~~~~~~~~~~~~~

"""
import os
import logging

class BaseConfig:
    """Base Configuration"""
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOGGING_LOCATION = "flask-base.log"
    LOGGING_LEVEL = logging.DEBUG
    SECRET_KEY = os.getenv("SECRET_KEY")
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 0
    TOKEN_PASSWORD_EXPIRATION_DAYS = 1
    TOKEN_PASSWORD_EXPIRATION_SECONDS = 0
    MONGODB_HOST = os.getenv("MONGO_URI")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "false").lower() == "true"
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "false").lower() == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_SENDER = os.getenv("MAIL_SENDER")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    SWAGGER={
        "openapi": "3.0.0"
    }
    JWT_AUTH_HEADER_NAME = "Authorization"


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    SECRET_KEY = "viva la pluto"


class TestingConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 3
    TOKEN_PASSWORD_EXPIRATION_DAYS = 0
    TOKEN_PASSWORD_EXPIRATION_SECONDS = 2
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_TEST_URL")


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    DEBUG = False
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")

