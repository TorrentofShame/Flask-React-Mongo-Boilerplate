import json
from mongoengine.errors import NotUniqueError
from server.models.user import User
from test.base import BaseTestCase


class TestFlasgger(BaseTestCase):

    def test_get_apidocs(self):
        """The GET on /apidocs should return 200"""
        res = self.client.get("/apidocs/")
        self.assertEqual(res.status_code, 200)

    def test_flasgger_is_not_empty(self):
        """The GET on /apispec_1.json should return a dict with a non-empty paths property"""
        res = self.client.get("/apispec_1.json")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode())
        self.assertTrue(data["paths"])
