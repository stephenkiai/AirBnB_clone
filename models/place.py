#!/usr/bin/env python3

"""
This is the Place module for the AirBnb_clone project.

Module functionality:
- Provides the Place class, which represents an accommodation place.
- Inherits from the BaseModel class.

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This is the Place class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Place class.

        Parameters:
        - args: Positional arguments (not used in this implementation).
        - kwargs: Keyword arguments that can be used to initialize the
        instance attributes.

        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
