#!/usr/bin/env python3
"""Test suite for Amenity class of the models.amenity module"""

import unittest

from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_subclass_of_base(self):
        self.assertTrue(issubclass(BaseModel, type(self.amenity)))

    def test_is_a_class(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))