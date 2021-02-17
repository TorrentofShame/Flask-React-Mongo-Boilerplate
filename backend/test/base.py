# flake8: noqa
import os
os.environ["APP_SETTINGS"] = "server.config.TestingConfig"
from flask_testing import TestCase
from mongoengine import connect
from mongoengine.connection import disconnect_all, get_db
from server import app


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object("server.config.TestingConfig")
        return app

    @classmethod
    def setUpClass(cls):
        disconnect_all()
        cls._conn = connect("mongoenginetest", host="mongomock://localhost")
        cls._conn.drop_database("mongoenginetest")

    @classmethod
    def tearDownClass(cls):
        cls._conn.drop_database("mongoenginetest")
        disconnect_all()

    def tearDown(self):
        self._conn.drop_database("mongoenginetest")
