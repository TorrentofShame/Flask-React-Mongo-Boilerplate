# -*- coding: utf-8 -*-
"""
    server.api.users
    ~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, request, render_template

from server.models.user import User, UserRole
from server import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/ping", methods=["GET"])
def heartbeat():
    """
    Heartbeat
    ---
    tags:
      - users
    responses:
      200:
        description: Heartbeat
        schema:
          id: rex_heartbeat
          properties:
            message:
                type: string
                description: The thing you are
                default: 'pong!'
    """
    return {
        "status": "success",
        "message": "pong!"
    }

@users_blueprint.route("/<username>", methods=["GET"])
def get_user(username):
    """
    This is a test.
    ---
    tags:
      - users
    parameters:
      - in: path
        name: username
        type: string
        required: true
    responses:
      200:
        description: A single user item
        schema:
          id: rec_username
          properties:
            username:
              type: string
              description: The name of the user
              default: 'john-smith'
    """
    return {"username": username}

