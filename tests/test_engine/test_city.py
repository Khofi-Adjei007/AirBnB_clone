#!/usr/bin/python3
"""
Defines unit tests for models/city.py.

Unittest classes:
    TestCityInstantiation
    TestCitySave
    TestCityToDict
"""

import os
import unittest
from datetime import datetime
from time import sleep

from models.city import City
import models


class TestCityInstantiation(unittest.TestCase):

    """
    Unittests for testing instantiation of the City class.
    """

    def test_no_args_instantiates(self):
        """Test that City instance can be created with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that new City instance is stored in models.storage."""
        self.assertIn(City(), models.storage.all().values())

    # ... (other test methods)


class TestCitySave(unittest.TestCase):

    """
    Unittests for testing save method of the City class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    # ... (other test methods)


class TestCityToDict(unittest.TestCase):

    """
    Unittests for testing to_dict method of the City class.
    """

    def test_to_dict_type(self):
        """Test that to_dict method returns a dictionary."""
        cy = City()
        self.assertTrue(dict, type(cy.to_dict()))

    # ... (other test methods)


if __name__ == "__main__":
    unittest.main()
