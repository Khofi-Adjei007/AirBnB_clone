#!/usr/bin/python3
"""City Class Definition"""

from models.base_model import BaseModel


class City(BaseModel):

    """Class representing city objects"""

    # Initialize the state_id and name attributes
    state_id = ""
    name = ""
