# -*- coding: utf-8 -*-
"""
    server.api.hackers
    ~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, request
from werkzeug.exceptions import BadRequest

from server.common.decorators import authenticate_user
from server.models.hacker import Hacker
from server import db

hackers_blueprint = Blueprint("hackers", __name__)

##### Hacker Management #####

@hackers_blueprint.route("/", methods=["POST"])
@authenticate_user
def create_hacker():
    """
    Creates a new Hacker.
    ---
    tags:
      - hacker
    summary: Create Hacker
    requestBody:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Hacker'
      description: Created hacker object
      required: true
    responses:
      default:
        description: successful operation
    """
    data = request.get_json()
    if not data:
        raise BadRequest()
    res = {
        "status": "success",
        "message": "hacker was added!"
    }
    return res, 201

@hackers_blueprint.route("/<hacker_id>", methods=["GET"])
@authenticate_user
def get_hacker(hacker_id):
    """
    Gets a Hacker.
    ---
    tags:
      - hacker
    summary: Gets a Hacker
    parameters:
      - id: hacker_id
        in: path
        description: The id that needs to be fetched.
        required: true
        schema:
          type: string
    responses:
      200:
        description: Successful Operation
        content:
          application/json:
            schema:
              $ref: "#components/schemas/Hacker"
      400:
        description: Invalid hacker_id supplied
      404:
        description: Hacker not found
    """
    pass

@hackers_blueprint.route("/<hacker_id>", methods=["PUT"])
@authenticate_user
def update_hacker(hacker_id):
    """
    Updates a Hacker.
    ---
    tags:
      - hacker
    summary: Updates a Hacker
    parameters:
      - id: hacker_id
        in: path
        description: The id that needs to be updated.
        required: true
        schema:
          type: string
    requestBody:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Hacker'
    responses:
      400:
        description: Invalid hacker_id supplied
      404:
        description: Hacker not found
    """
    pass

@hackers_blueprint.route("/<hacker_id>", methods=["DELETE"])
@authenticate_user
def delete_hacker(hacker_id):
    """
    Deletes a Hacker.
    ---
    tags:
      - hacker
    summary: Deletes a Hacker
    parameters:
      - id: hacker_id
        in: path
        description: The id of the hacker to be deleted.
        required: true
        schema:
          type: string
    responses:
      400:
        description: Invalid hackername supplied.
      404:
        description: Hacker not found.
    """
    pass


@hackers_blueprint.route("/all", methods=["GET"])
@authenticate_user
def get_all_hackers():
    """
    Get all Hackers.
    ---
    tags:
      - hacker
    summary: Gets all Hackers
    responses:
      200:
        description: Successful Operation
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Hacker'
    """
    hackers = Hacker.objects.exclude("id", "password").to_json()
    return hackers, 200

