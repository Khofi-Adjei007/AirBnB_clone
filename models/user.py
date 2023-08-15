#!/usr/bin/python3
"""Module defining the User class."""

from models.base_model import BaseModel


class User(BaseModel):

    """A class representing user objects for management."""

    email = ""  # Placeholder for the user's email
    password = ""  # Placeholder for the user's password
    first_name = ""  # Placeholder for the user's first name
    last_name = ""  # Placeholder for the user's last name
