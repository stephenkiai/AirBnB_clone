#!/usr/bin/env python3

"""
This is the State module for the AirBnb_clone project.

Module functionality:
- Provides the State class, which represents a state or province.
- Inherits from the BaseModel class.

"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the State class.

        Parameters:
        - args: Positional arguments (not used in this implementation).
        - kwargs: Keyword arguments that can be used to initialize the
        instance attributes.

        """

        super().__init__(*args, **kwargs)
        self.name = ""
