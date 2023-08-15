#!/usr/bin/python3
"""Module defining the Place class."""

from models.base_model import BaseModel


class Place(BaseModel):

    """A class representing place objects for management."""

    city_id = ""  # Placeholder for the associated city ID
    user_id = ""  # Placeholder for the associated user ID
    name = ""  # Placeholder for the place name
    description = ""  # Placeholder for the place description
    number_rooms = 0  # Placeholder for the number of rooms
    number_bathrooms = 0  # Placeholder for the number of bathrooms
    max_guest = 0  # Placeholder for the maximum number of guests
    price_by_night = 0  # Placeholder for the price per night
    latitude = 0.0  # Placeholder for the latitude coordinate
    longitude = 0.0  # Placeholder for the longitude coordinate
    amenity_ids = []  # Placeholder for the list of amenity IDs
