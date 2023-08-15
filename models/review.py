#!/usr/bin/python3
"""Module defining the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):

    """A class representing review objects for management."""

    place_id = ""  # Placeholder for the associated place ID
    user_id = ""  # Placeholder for the associated user ID
    text = ""  # Placeholder for the review text
