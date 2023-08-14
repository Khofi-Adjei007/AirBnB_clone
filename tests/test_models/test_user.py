#!/usr/bin/python3

"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
from datetime import datetime
import models
import unittest
from models.user import User
from time import sleep


class TestUser_instantiation(unittest.TestCase):

    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    # ... Other test methods ...


class TestUser_save(unittest.TestCase):

    """Unittests for testing save method of the User class."""

    @classmethod
    def setUp(self):
        """Set up test class by renaming file.json to tmp."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tear down test class by restoring file.json from tmp."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    # ... Other test methods ...


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertIsInstance(User().to_dict(), dict)

    # ... Other test methods ...


if __name__ == "__main__":
    unittest.main()
