#!/usr/bin/python3

"""Defines unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):

    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        """Test that an instance can
        be created with no arguments
        """
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance is stored
        in the objects dictionary.
        """
        self.assertIn(Review(), models.storage.all().values())

    # ... Other tests ...


class TestReviewSave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class by renaming file.json to tmp."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        """
        Tear down test class by restoring
        file.json from tmp.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    # ... Other tests ...


class TestReviewToDict(unittest.TestCase):
    """
    Unittests for testing to_dict
    method of the Review class.
    """

    def test_to_dict_type(self):
        """Test that to_dict returns a dictionary."""
        self.assertIsInstance(Review().to_dict(), dict)

    # ... Other tests ...


if __name__ == "__main__":
    unittest.main()
