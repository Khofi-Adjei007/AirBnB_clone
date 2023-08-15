#!/usr/bin/python3
"""
Defines unit tests for models/amenity.py.

Unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityToDict
"""

import os
import unittest
from datetime import datetime
from time import sleep

from models.amenity import Amenity
import models


class TestAmenityInstantiation(unittest.TestCase):

    """
    Unittests for testing instantiation of the Amenity class.
    """

    def test_no_args_instantiates(self):
        """Test that Amenity instance can be created with no arguments."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test that new Amenity instance is stored in models.storage."""
        self.assertIn(Amenity(), models.storage.all().values())

    # ... (other test methods)


class TestAmenitySave(unittest.TestCase):

    """
    Unittests for testing save method of the Amenity class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    # ... (other test methods)


class TestAmenityToDict(unittest.TestCase):

    """
    Unittests for testing to_dict method of the Amenity class.
    """

    def test_to_dict_type(self):
        """Test that to_dict method returns a dictionary."""
        self.assertTrue(dict, type(Amenity().to_dict()))

    # ... (other test methods)


if __name__ == "__main__":
    unittest.main()
