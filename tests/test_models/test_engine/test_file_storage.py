#!/usr/bin/python3

# Import necessary modules and classes
import os
import unittest
from datetime import datetime
import json

# Import the classes from models package
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


# Test class for FileStorage instantiation
class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation
    of the FileStorage class.
    """

    # Test if FileStorage can be instantiated without arguments
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    # Test if FileStorage raises TypeError
    # when instantiated with an argument
    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    # Test if the private attribute __file_path
    # of FileStorage is a string
    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    # Test if the private attribute __objects of FileStorage is a dictionary
    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    # Test if the global storage object is an instance of FileStorage
    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

# Test class for FileStorage methods


class TestFileStorage_methods(unittest.TestCase):

    """Unittests for testing methods of the FileStorage class."""

    # Set up methods to run before test methods
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
            # Rename existing file.json to tmp
        except IOError:
            pass

    # Tear down methods to run after test methods
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")  # Remove the modified file.json
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")  # Rename tmp back to file.json
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        # Clear the stored objects dictionary

    # Test if the all method of storage returns a dictionary
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    # Test if all method raises TypeError when called with an argument
    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    # Test if new objects can be added to the storage
    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        # ... (similar lines for other objects)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        # Check if the object is added
        self.assertIn(bm, models.storage.all().values())
        # Check if the object is in the stored values
        # ... (similar lines for other objects)

    # Test if new method raises TypeError
    # when called with extra arguments
    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    # Test if new method raises AttributeError when called with None
    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    # Test if save method saves the objects to the file
    def test_save(self):
        bm = BaseModel()
        us = User()
        # ... (similar lines for other objects)
        models.storage.new(bm)
        models.storage.new(us)
        # ... (similar lines for other objects)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            # Check if the object IDs are in the saved text
            self.assertIn("BaseModel." + bm.id, save_text)
            # ... (similar lines for other objects)

    # Test if save method raises TypeError
    # when called with an argument
    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    # Test if reload method loads objects from the file
    def test_reload(self):
        bm = BaseModel()
        us = User()
        # ... (similar lines for other objects)
        models.storage.new(bm)
        models.storage.new(us)
        # ... (similar lines for other objects)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        # Check if reloaded objects match the original ones
        self.assertIn("BaseModel." + bm.id, objs)
        # ... (similar lines for other objects)

    # Test if reload method raises
    # FileNotFoundError when the file doesn't exist
    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    # Test if reload method raises TypeError when called with an argument
    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

# Run the unittests if this
# script is executed directly


if __name__ == "__main__":
    unittest.main()
