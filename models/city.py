#!/usr/bin/python3

"""Module defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):

    """
    Class representing a city.

    Attributes:
        state_id (str): The state
        ID associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""i
