#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from models.place import Place

"""
Test suit for place model
"""

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_subclass_of_base(self):
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_is_a_class(self):
        self.assertTrue(hasattr(self.place, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), float)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()