# -*- coding: utf-8 -*-
"""
    server.models.user
    ~~~~~~~~~~~~~~~~~~

"""
from flask import current_app
import jwt
from datetime import datetime, timedelta
from werkzeug.exceptions import Forbidden
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
        
    @staticmethod
    def findOne(*args, **kwargs):
        """Finds one User"""
        excludes = kwargs.pop("excludes", [])
        return User.objects(*args, **kwargs).exclude("id", *excludes).first()

    def encode_auth_token(self) -> str:
        """Generates the auth token"""
        expires_at = datetime.utcnow() + timedelta(
            days=current_app.config["TOKEN_EXPIRATION_DAYS"],
            seconds=current_app.config["TOKEN_EXPIRATION_SECONDS"]
        )
        payload = {
            "exp": expires_at,
            "iat": datetime.utcnow(),
            "sub": self.username
        }
        return jwt.encode(
            payload,
            current_app.config.get("SECRET_KEY"),
            algorithm="HS256"
        ), expires_at
    
    @staticmethod
    def decode_auth_token(auth_token):
        """Decodes the auth token"""
        try:
            payload = jwt.decode(auth_token, current_app.config.get("SECRET_KEY"))
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return Forbidden()
        except jwt.InvalidTokenError:
            return Forbidden()
    