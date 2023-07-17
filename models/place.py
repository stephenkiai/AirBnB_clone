#!/usr/bin/env python3
"""
- Provides the Place class, which represents an accommodation place.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This is the Place class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Place class.
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
