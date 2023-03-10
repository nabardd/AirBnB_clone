#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from models.user import User

"""Test for user Model"""

class Testuser(unittest.TestCase):

    """
    Test suite for user model
    """

    def setUp(self):
        self.user = User()

    def test_is_subclass(self):
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_is_class(self):
        self.assertTrue(hasattr(self.user, "first_name"))

    def test_attrs(self):
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)

if __name__ == "__main__":
    unittest.main()