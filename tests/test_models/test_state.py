#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""

import os
import datetime
import unittest
from time import sleep

from models import models
from models.state import State


class TestStateInstantiation(unittest.TestCase):

    """
    Unittests for testing instantiation
    of the State class.
    """

    def test_no_args_instantiates(self):
        """Test that an instance can be created with no arguments."""
        self.assertEqual(State, type(State()))

    # ... Other test methods ...


class TestStateSave(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class by renaming file.json to tmp."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
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


class TestStateToDict(unittest.TestCase):
    """
    Unittests for testing to_dict method
    of the State class.
    """

    def test_to_dict_type(self):
        """Test that to_dict returns a dictionary."""
        self.assertIsInstance(State().to_dict(), dict)

    # ... Other test methods ...


if __name__ == "__main__":
    unittest.main()
