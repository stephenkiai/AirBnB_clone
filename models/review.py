#!/usr/bin/env python3

"""
This is the Review module for the AirBnb_clone project.

Module functionality:
- Provides the Review class, which represents a review for an
accommodation place.
- Inherits from the BaseModel class.

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the Review class.

        Parameters:
        - args: Positional arguments (not used in this implementation).
        - kwargs: Keyword arguments that can be used to initialize the
        instance attributes.

        """

        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
