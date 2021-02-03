# -*- coding: utf-8 -*-
"""
    server.api.auth
    ~~~~~~~~~~~~~~~

"""
from flask import Blueprint, request
from werkzeug.exceptions import BadRequest

# from server.models.User import User, UserRole
# from server import db

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login_user():
    """
    Logs in User
    ---
    tags:
      - auth
    summary: Logs in User
    responses:
      200:
        description: User was logged in successfully.
        headers:
          X-Expires-After:
            description: Date in UTC when token expires.
            schema:
              type: string
              format: date-time
      400:
        description: User login failed.
    requestBody:
      content:
        application/json:
          schema:
            type: object
            properties:
              email:
                type: string
                example: foo@bar.com
              password:
                type: string
                format: password
    """
    data = request.get_json()
    if not data:
        raise BadPayload()
    res = {
        "status": "success",
        "message": "hacker was added!"
    }
    return res, 200


@auth_blueprint.route("/logout", methods=["GET"])
def logout_user():
    """
    Logs out the current user.
    ---
    tags:
      - auth
    summary: Logs out the current user.
    responses:
      default:
        description: Successful Operation
    """
    pass
