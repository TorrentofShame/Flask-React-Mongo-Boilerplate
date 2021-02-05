# -*- coding: utf-8 -*-
"""
    server.api.auth
    ~~~~~~~~~~~~~~~

"""
from flask import Blueprint, request, current_app
import jwt
from werkzeug.exceptions import BadRequest, Forbidden, NotFound
from server.models.user import User, UserRole
from server.common.utils import authenticate
from server import bcrypt

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
        content:
          application/json:
            schema:
              type: object
              properties:
                auth_token:
                  type: string
                  example: abcde123456
                message:
                  type: string
                  example: User was logged in!
                status:
                  type: string
                  example: success
      400:
        description: User login failed.
    requestBody:
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                example: foobar
              password:
                type: string
                format: password
    """
    data = request.get_json()
    if not data: raise BadPayload()
    if not data.get("password"): raise BadPayload()
        
    user = User.objects(username=data["username"]).exclude("id").first()
    if not user: raise NotFound()
    
    if not bcrypt.check_password_hash(user.password, data["password"]):
        raise Forbidden()
    auth_token, expire_date = user.encode_auth_token()
    

    res = {
        "status": "success",
        "message": "user was logged in!",
        "auth_token": auth_token.decode()
    }
    return res, 200, [("X-Expires-After", expire_date)]


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
