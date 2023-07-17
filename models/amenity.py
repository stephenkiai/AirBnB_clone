#!/usr/bin/env python3
"""
- Provides the Amenity class,represents an amenity for accommodations.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    - Represents an amenity for accommodations.
    """

    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the Amenity class.
        """

        super().__init__(*args, **kwargs)
        self.name = ""
