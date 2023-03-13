#!/usr/bin/env python3
"""
A module that contains the test suite for the BaseModel class
"""

import unittest
from time import sleep
import os
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test Suite for models.base_model.BaseModel
    """

    def test_has_id(self):
        """
        Checks that instance has an id assigned on initialization
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
    
    def test_str_rep(self):
        """
        Tests if string representation for class is 
        appropriate
        """
        b = BaseModel()
        str_rep = str(b)
        self.assertTrue(
            str_rep, f"[BaseModel] ({b.id}) {b.__dict__}")
        
    def test_unique_ids(self):
        """
        Test to check if ids are unique
        """

        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_type_str(self):
        """
        Test to check data type of id is str
        """

        b = BaseModel()
        self.assertTrue(isinstance(b.id, str))

    def test_created_at_datetime(self):
        """
        Test to check if created at is a datetime object
        """

        b = BaseModel()
        self.assertTrue(isinstance(b.created_at, datetime))

    def test_updated_at_datetime(self):
        """
        Test to check that updates at is a datetime object
        """

        b = BaseModel()
        self.assertTrue(isinstance(b.updated_at, datetime))

    def test_different_created_at(self):
        """
        Test to check if created at for two models are different
        """

        b1 = BaseModel()
        sleep(1)

        b2 = BaseModel()
        sleep(1)

        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_no_args(self):
        """
        Test to check performance when no args where passed
        """

        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_created_at_and_updated_at_equal_at_init(self):
        """
        Test to check
        <class>.created_at == <class>.updated_at
        at initialization
        """
        b = BaseModel()

        self.assertEqual(b.created_at, b.updated_at)

    def test_save_func_updates(self):
        """
        Checking if save() updates the updated_at attr
        """

        b = BaseModel()
        sleep(0.2)
        b.save()

        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertGreater(
            b.updated_at.microsecond(),
            b.created_at.microsecond()
            )

    def test_to_dict_returns_dict(self):
        """
        Tests if to_dict() returns a dictionary
        """

        b = BaseModel()
        b_dict = b.to_dict()

        self.assertTrue(isinstance(b_dict, dict))

    def test_to_dict_returns_class_dunder(self):
        """
        Test to check if to_dict returns __class__
        dunder method
        """
        b = BaseModel()
        self.assertTrue("__class__" in b.to_dict())

    def test_to_dict_created_at_is_ISO(self):
        """
        Test to check if created at in dict returned by
        to_dict is in the ISO format
        """

        b = BaseModel()
        base_dict = b.to_dict()
        self.assertEqual(base_dict['created_at'], b.created_at.isoformat())

    def test_to_dict_updated_at_is_ISO(self):
        """
        Test to check if created at in dict returned by to_dict
        is in the ISO format
        """

        b = BaseModel()
        base_dict = b.to_dict()
        self.assertEqual(base_dict['updated_at'], b.updated_at.isoformat())

    def test_empty_kwargs(self):
        """
        Test to check for when kwargs passed is empty
        """
        k_dict = {}
        b = BaseModel(**k_dict)
        self.assertTrue(isinstance(b.name, str))
        self.assertTrue(isinstance(b.created_at, datetime))
        self.assertTrue(isinstance(b.created_at, datetime))

    def test_not_empty_kwargs(self):
        """
        checks that fields are created from kwargs
        """
        k_dict = {
            "id": uuid4(),
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }
        b = BaseModel(**k_dict)

        self.assertEqual(b.id, k_dict["id"])
        self.assertEqual(b.created_at,
                        datetime.strptime(k_dict["created_at"],
                                        "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(b.updated_at, 
                        datetime.strptime(k_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        
    def test_kwargs_and_args_provided(self):
        """
        Test to check when kwargs and args
        """
        date = datetime.now().isoformat()
        b = BaseModel(
            id = "53",
            created_at = date,
            updated_at = date,
            name = "David"
        )

        self.assertEqual(b.id, "53")
        self.assertEqual(b.created_at, date)
        self.assertEqual(b.updated_at, date)
        self.assertEqual(b.name, "David")

    def test_to_dict_ouput(self):
        """
        Checks output returned by to_dict()
        """

        b = BaseModel()
        date = datetime.now()
        b.id = '12233'
        b.created_at = b.updated_at = date
        demo_output = {
            'id': '12233',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
            '__class__': 'BaseModel'
        }

        self.assertDictEqual(b.to_dict(), demo_output)

    def test_to_dict_with_args(self):
        """
        Check when to_dict is passed with args
        """

        b = BaseModel()

        with self.assertRaises(TypeError):
            b.to_dict(None)


if __name__ == "__main__":
    unittest.main()