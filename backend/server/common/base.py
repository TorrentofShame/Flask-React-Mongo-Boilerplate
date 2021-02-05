# -*- coding: utf-8 -*-
"""
    server.common.base
    ~~~~~~~~~~~~~~~~~~

"""
import os
import logging
import datetime

from flask import Flask, jsonify, Response
from flask.json import JSONEncoder
from flask_cors import CORS


class JSONEncoderBase(JSONEncoder):
    """Custom Encoder to handle datetime as ISO8601 format"""

    def default(self, obj):
        try:
            if isinstance(obj, datetime.date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


class ResponseBase(Response):
    # default_mimetype = "application/json"

    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(ResponseBase, cls).force_type(rv, environ)


class FlaskBase(Flask):
    response_class = ResponseBase
    json_encoder = JSONEncoderBase

    def __init__(self, import_name):

        Flask.__init__(self, import_name)

        # Set Config
        app_settings = os.getenv("APP_SETTINGS", "server.config.DevelopmentConfig")
        self.config.from_object(app_settings)

        # Setup Logging
        handler = logging.FileHandler(self.config.get("LOGGING_LOCATION"))
        handler.setLevel(self.config["LOGGING_LEVEL"])
        handler.setFormatter(logging.Formatter(self.config.get("LOGGING_FORMAT")))
        self.logger.addHandler(handler)

        # Enable CORS
        CORS(self)

