# -*- coding: utf-8 -*-
"""
    server.common.decorators
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import request
from functools import wraps
from werkzeug.exceptions import Unauthorized, Forbidden

from server.models.user import User, UserRole

def authenticate_user(f):
    
    if doc := getattr(f, "__doc__"):
        setattr(f, "__doc__", doc + """security:
        - ApiKeyAuth: []""")
    
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_token = request.headers.get("Authorization")
        if not auth_token:
            raise Unauthorized
        username = User.decode_auth_token(auth_token)
        user = User.findOne(username=username)
        if not user:
            raise Unauthorized()
        return f(username, *args, **kwargs)
    return decorator


def authenticate_hacker(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        return f(user_id, *args, **kwargs)
    return decorator

def user_privileges(roles): # TODO: Make this work for at least this role.
    def decorator(f):
        @wraps(f)
        def decorated_function(username, *args, **kwargs):
            user = User.findOne(username=username, excludes=["password"])
            if not user:
                raise Unauthorized()
            user_role = user.role
            if user_role not in roles:
                raise Forbidden()
            return f(username, *args, **kwargs)
        return decorated_function
    return decorator
