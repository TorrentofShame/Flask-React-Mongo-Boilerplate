# -*- coding: utf-8 -*-
"""
    server.common.exceptions
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""

class APIException(Exception):
    """A Base Exception for API use"""

    def __init__(self, message, status_code, payload):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        rv["status"] = "error"
        return rv


class InvalidPayload(APIException):
    """400 status code"""

    def __init__(self, message="Invalid payload.", payload=None):
        super().__init__(message=message, status_code=400, payload=payload)


class BusinessException(APIException):
    """400 status code"""

    def __init__(self, message="Business rule constraint not satisfied", payload=None):
        super().__init__(message=message, status_code=400, payload=payload)


class UnauthorizedException(APIException):
    """401 status code"""

    def __init__(self, message="Not Authorized.", payload=None):
        super().__init__(message=message, status_code=401, payload=payload)


class ForbiddenException(APIException):
    """403 status code"""

    def __init__(self, message="Forbidden.", payload=None):
        super().__init__(message=message, status_code=403, payload=payload)


class TeapotException(APIException):
    """418 status code use for Automated Requests & Rate Limiting."""

    def __init__(self, message="I'm a teapot.", payload=None):
        super().__init__(message=message, status_code=418, payload=payload)


class NotFoundException(APIException):
    """404 status code use for Automated Requests & Rate Limiting."""
    code = 404
    def __init__(self, message="I'm a teapot.", payload=None):
        super().__init__(message=message, status_code=404, payload=payload)


class ServerErrorException(APIException):
    """500 status code"""

    def __init__(self, message="Something went wrong.", payload=None):
        super().__init__(message=message, status_code=500, payload=payload)

