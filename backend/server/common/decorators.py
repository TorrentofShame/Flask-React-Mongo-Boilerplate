# -*- coding: utf-8 -*-
"""
    server.common.decorators
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import request

from server.common.exceptions import UnauthorizedException, ForbiddenException

def authenticate(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise UnauthorizedException()
        auth_token = auth_header.split(" ")[1]
        user_id = User.decode_auth_token(auth_token)
        user = User.get(user_id)
        if not user or not user.active:
            raise UnauthorizedException(message="Something went wront. Please contact us.")
        return f(user_id, *args, **kwargs)
    return decorator

