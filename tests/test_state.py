#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from models.state import State

"""Test for state Model"""


class Teststate(unittest.TestCase):

    """
    Test suite for state model
    """

    def setUp(self):
        self.state = State()

    def test_is_subclass(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_is_class(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_attrs(self):
        self.assertIs(type(self.state.name), str)


if __name__ == "__main__":
    unittest.main()
