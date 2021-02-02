# -*- coding: utf-8 -*-
"""
    server.models.user
    ~~~~~~~~~~~~~~~~~~

"""
from enum import Enum
from server import db

UserRole = ("USER", "ADMIN")

class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.EmailField(unique=True)
    role = db.StringField(choices=UserRole)
