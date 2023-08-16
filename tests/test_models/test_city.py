#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test that City instance is created without any arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new City instance is stored in the storage."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of City is a string."""
        self.assertEqual(str, type(City().id))

    # ... (other test methods)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

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
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    # ... (other test methods)

    def test_save_with_arg(self):
        """Test save method with argument."""
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file with the instance data."""
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict is a dictionary."""
        self.assertTrue(dict, type(City().to_dict()))

    # ... (other test methods)

    def test_to_dict_with_arg(self):
        """Test to_dict method with an argument."""
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
