#!/usr/bin/python3

"""Module defining the FileStorage class."""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:

    """
    Class representing an abstracted storage engine.

    Attributes:
        __objects (dict): Dictionary of instantiated objects.
        __file_path (str): The file path to save objects.
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
        Return the dictionary __objects containing all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set the object in __objects with key <obj_class_name>.id.
        """
        object_class_name = obj.__class__.__name__
        FileStorage.__objects[f"{object_class_name}.{obj.id}"] = obj

    def save(self):
        """
        Serialize __objects to the JSON file __file_path.
        """
        objects_to_serialize = {
                obj_id: obj.to_dict()
                for obj_id, obj in FileStorage.__objects.items()
                }

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_to_serialize, file)

    def reload(self):
        """
        Deserialize the JSON file __file_path
        to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            return
