#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from models.review import Review

"""Test for Review Model"""

class TestReview(unittest.TestCase):

    """
    Test suite for Review model
    """

    def setUp(self):
        self.review = Review()

    def test_is_subclass(self):
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_is_class(self):
        self.assertTrue(hasattr(self.review, "name"))

    def test_attrs(self):
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.user_id), str)
        self.assertIs(type(self.review.text), str)

if __name__ == "__main__":
    unittest.main()