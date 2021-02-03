# -*- coding: utf-8 -*-
"""
    server.models.hacker
    ~~~~~~~~~~~~~~~~~~~~

"""
from server.common.validators import validate_phone_number
from server import db


class HackerEmergencyContact(db.EmbeddedDocument):
    first_name = db.StringField()
    last_name = db.StringField()
    phone_number = db.StringField(validation=validate_phone_number)
    relationship = db.StringField()


class HackerProfile(db.EmbeddedDocument):
    gender = db.StringField()
    ethnicity = db.StringField()
    pronouns = db.StringField()
    school = db.StringField()
    expected_graduation = db.DateTimeField()
    why_attend = db.StringField(max_length=200)
    what_learn = db.StringField(max_length=200)
    will_need_travel = db.BooleanField()


class Hacker(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    username = db.StringField(unique=True)
    password = db.StringField()
    email = db.EmailField(unique=True)
    phone_number = db.StringField(validation=validate_phone_number)
    profile = db.EmbeddedDocumentField(HackerProfile)
    resume = db.URLField()
    emergency_contact = db.EmbeddedDocumentField(HackerEmergencyContact)
    accepted_forms = db.BooleanField()
    active_participant = db.BooleanField()

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "phone_number": self.phone_number,
            "profile": self.profile,
            "resume": self.resume,
            "emergency_contact": self.emergency_contact,
            "accepted_forms": self.accepted_forms,
            "active_participant": self.active_participant
        }
