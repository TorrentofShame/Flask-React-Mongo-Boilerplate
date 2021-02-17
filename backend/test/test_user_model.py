from mongoengine.errors import NotUniqueError
from server.models.user import User
from test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_create_user(self):
        user = User(username="foobar",
                    email="foobar@email.com",
                    password="password")
        user.save()
        self.assertTrue(user.id)
        self.assertEqual(user.username, "foobar")
        self.assertEqual(user.email, "foobar@email.com")
        self.assertTrue(user.password)

    def test_create_user_duplicate_username(self):
        user = User(username="foobar",
                    email="foobar@email.com",
                    password="password")
        user.save()
        duplicate_user = User(username="foobar",
                              email="foobar2@email.com",
                              password="password")
        self.assertRaises(NotUniqueError, duplicate_user.save)

    def test_create_user_duplicate_email(self):
        user = User(username="foobar",
                    email="foobar@email.com",
                    password="password")
        user.save()
        duplicate_user = User(username="foobar2",
                              email="foobar@email.com",
                              password="password")
        self.assertRaises(NotUniqueError, duplicate_user.save)
