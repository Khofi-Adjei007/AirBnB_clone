#!/usr/bin/python3
"""Review Class Definition"""

from models.base_model import BaseModel


class Review(BaseModel):

    """Class representing review objects"""

    # Initialize attributes for review details
    place_id = ""
    user_id = ""
    text = ""
