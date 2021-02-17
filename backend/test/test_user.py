import json
from mongoengine.errors import NotUniqueError
from server.models.user import User
from test.base import BaseTestCase


class TestUsersBlueprint(BaseTestCase):
    """Tests for the Users Endpoints"""

    def test_users(self):
        """Ensure the ping route behaves correctly"""
        res = self.client.get("/api/users/ping", headers=[("Accept", "application/json")])
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertIn("Pong!", data["message"])
