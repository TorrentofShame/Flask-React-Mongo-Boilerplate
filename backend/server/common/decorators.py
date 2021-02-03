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
    @wraps(f)
    def decorator(*args, **kwargs):

        return f(user_id, *args, **kwargs)
    return decorator


def authenticate_hacker(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        return f(user_id, *args, **kwargs)
    return decorator

def user_privileges(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(loggedin_username, *args, **kwargs):
            return f(loggedin_username, *args, **kwargs)
        return decorated_function
    return decorator
