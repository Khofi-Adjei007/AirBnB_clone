#!/usr/bin/python3
"""User Class Definition"""

from models.base_model import BaseModel


class User(BaseModel):

    """Class representing user objects"""

    # Initialize attributes for user details
    email = ""
    password = ""
    first_name = ""
    last_name = ""
