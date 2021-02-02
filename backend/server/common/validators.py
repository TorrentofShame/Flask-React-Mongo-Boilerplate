# -*- coding: utf-8 -*-
"""
    server.common.validators
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""

def validate_phone_number(phone_number: str):
    """Validates Phone Number Strings"""
    if not phone_number.isdecimal() or len(phone_number) != 10:
        raise ValidationError("Value is not a 10-digit phone number!")
