#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from models.city import City

"""
Test Suite for city model
"""

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_subclass_of_base(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_is_a_class(self):
        self.assertTrue(hasattr(self.city, "name"))

    def test_class_attrs(self):
        self.assertTrue(type(self.city.state_id), str)
        self.assertTrue(type(self.city.name), str)

if __name__ == "__main__":
    unittest.main()