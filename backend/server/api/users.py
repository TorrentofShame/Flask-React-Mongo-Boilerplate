# -*- coding: utf-8 -*-
"""
    server.api.users
    ~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from werkzeug.exceptions import BadRequest, NotFound

from server.models.user import User, UserRole
from server import db

users_blueprint = Blueprint("users", __name__)


##### User Management #####

@users_blueprint.route("/", methods=["POST"])
@jwt_required()
def create_user():
    """
    Creates a new User.
    ---
    tags:
      - user
    summary: Create User
    requestBody:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/User'
      description: Created user object
      required: true
    responses:
      default:
        description: successful operation
      400:
        description: email already exists
    """
    data = request.get_json()
    if not data:
        raise BadRequest()
    user = User(**data)
    user.save()
    res = {
        "status": "success",
        "message": "user was added!"
    }
    return res, 201

@users_blueprint.route("/<username>", methods=["GET"])
@jwt_required()
def get_user(username):
    """
    Gets a User.
    ---
    tags:
      - user
    summary: Gets a User
    parameters:
      - id: username
        in: path
        description: The username of the user to be fetched.
        required: true
        schema:
          type: string
    responses:
      200:
        description: Successful Operation
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: success
                data:
                  $ref: "#components/schemas/User"
      400:
        description: Invalid username supplied
      404:
        description: User not found
    """
    user = User.objects(username=username).exclude("id", "password").first()
    if not user:
        raise NotFound(description="User does not exist.")
    res = {
        "status": "success",
        "data": user
    }
    return res, 200


@users_blueprint.route("/<username>", methods=["PUT"])
@jwt_required()
def update_user(username):
    """
    Updates a User.
    ---
    tags:
      - user
    summary: Updates a User
    parameters:
      - id: username
        in: path
        description: The id that needs to be updated.
        required: true
        schema:
          type: string
    requestBody:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/User'
    responses:
      200:
        description: User updated successfully.
      400:
        description: Invalid username supplied
      404:
        description: User not found
      400:
        description: Email already exists.
    """
    update = request.get_json()
    if not update:
        raise BadRequest()
    user = User.object(username=username).first()
    if not user:
        raise NotFound()
    user.update(**update)
    res = {
        "status": "success",
        "message": "User successfully updated."
    }
    return res

@users_blueprint.route("/<username>", methods=["DELETE"])
@jwt_required()
def delete_user(username):
    """
    Deletes a User.
    ---
    tags:
      - user
    summary: Deletes a User
    parameters:
      - id: username
        in: path
        description: The username of the user to be deleted.
        required: true
        schema:
          type: string
    responses:
      200:
        description: User was successfully deleted.
      400:
        description: Invalid username supplied.
      404:
        description: User not found.
    """
    user = User.objects(username=username).first()
    if not user:
        raise NotFound()
    user.delete()
    res = {
        "status": "success",
        "message": "user was deleted!"
    }
    return res, 200

@users_blueprint.route("/all", methods=["GET"])
@jwt_required()
def get_all_users():
    """
    Get all Users
    ---
    tags:
      - user
    summary: Gets all Users
    responses:
      200:
        description: Successful Operation
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/User'
    """
    users = User.objects.exclude("id", "password").to_json()
    return users, 200

