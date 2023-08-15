#!/usr/bin/python3
"""
Defines unit tests for models/base_model.py.

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""

import os
import unittest
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
import models


class TestBaseModelInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the BaseModel class.
    """

    def test_no_args_instantiates(self):
        """Test that BaseModel instance can be created with no arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """Test that new BaseModel instance is stored in models.storage."""
        self.assertIn(BaseModel(), models.storage.all().values())

    # ... (other test methods)


class TestBaseModelSave(unittest.TestCase):

    """
    Unittests for testing save method of the BaseModel class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    # ... (other test methods)


class TestBaseModelToDict(unittest.TestCase):

    """
    Unittests for testing to_dict method of the BaseModel class.
    """

    def test_to_dict_type(self):
        """Test that to_dict method returns a dictionary."""
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    # ... (other test methods)


if __name__ == "__main__":
    unittest.main()
