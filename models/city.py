#!/usr/bin/env python3

"""
This is the City module for the AirBnb_clone project.

Module functionality:
- Provides the City class, which represents a city for accommodations.
- Inherits from the BaseModel class.

"""

from models.base_model import BaseModel


class City(BaseModel):

    """
    This is the City class that inherits from BaseModel.

    Class functionality:
    - Represents a city for accommodations.

    Attributes:
    - id: Unique identifier for each City instance.
    - created_at: Date and time when the City instance was created.
    - updated_at: Date and time when the City instance was last updated.
    - state_id: ID of the state that the city belongs to.
    - name: Name of the city.

    Methods:
    - __init__: Initializes a new instance of the City class.

    """

    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the City class.

        Parameters:
        - args: Positional arguments (not used in this implementation).
        - kwargs: Keyword arguments that can be used to initialize the
        instance attributes.

        """

        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
