#!/usr/bin/python3

"""Module defining the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """
    Class representing the BaseModel
    of the Airbnb project.

    Attributes:
        id (str): Unique identifier
        generated for each instance.
        created_at (datetime):
        Timestamp of instance creation.
        updated_at (datetime):
        Timestamp of instance update.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value
            pairs of attributes.
        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Update updated_at with the current datetime
        and save changes using the storage model.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation
        of the BaseModel instance.
        Includes the key/value pair '__class__'
        representing the class name.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)