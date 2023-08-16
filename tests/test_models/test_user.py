#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """Test that User instance is created without any arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new User instance is stored in the storage."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of User is a string."""
        self.assertEqual(str, type(User().id))

    # ... (other test methods)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def setUp(self):
        """Set up method to handle file renaming for testing."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tear down method to revert file renaming after testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test one-time save and updated_at change."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    # ... (other test methods)

    def test_save_with_arg(self):
        """Test save method with argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file with the instance data."""
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict is a dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    # ... (other test methods)

    def test_to_dict_with_arg(self):
        """Test to_dict method with an argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
