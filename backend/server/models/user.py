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
    username = db.StringField(unique=True)
    password = db.StringField()
    email = db.EmailField(unique=True)
    role = db.StringField(choices=UserRole)

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "role": self.role
        }
