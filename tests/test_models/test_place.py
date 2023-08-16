#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test that Place instance is created without any arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new Place instance is stored in the storage."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of Place is a string."""
        self.assertEqual(str, type(Place().id))

    # ... (other test methods)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    # ... (other test methods)

    def test_save_with_arg(self):
        """Test save method with argument."""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file with the instance data."""
        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict is a dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    # ... (other test methods)

    def test_to_dict_with_arg(self):
        """Test to_dict method with an argument."""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
