#!/usr/bin/python3

"""Module defining the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):

    """
    Class representing a review.

    Attributes:
        place_id (str): Tihe ID o
        the associated place.
        user_id (str): The ID of
        the user who wrote the review.
        text (str): The text
        content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
