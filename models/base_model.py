#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Dictionary of attribute names and
            values for initialization.
            If 'created_at' or 'updated_at' attributes
            are present in kwargs,
            they are converted from strings to datetime objects.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime): Timestamp when
            the instance was created.
            updated_at (datetime): Timestamp when
            the instance was last updated.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            self.created_at = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
            str: A formatted string containing the
            class name, ID, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the instance to a dictionary representation.

        Returns:
            dict: A dictionary containing all instance
            attributes and values.
                  'created_at' and 'updated_at'
                  attributes are converted to ISO format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
