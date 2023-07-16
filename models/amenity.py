#!/usr/bin/env python3

"""
This is the Amenity module for the AirBnb_clone project.

Module functionality:
- Provides the Amenity class, which represents an amenity for accommodations.
- Inherits from the BaseModel class.

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is the Amenity class that inherits from BaseModel.

    Class functionality:
    - Represents an amenity for accommodations.

    Attributes:
    - id: Unique identifier for each Amenity instance.
    - created_at: Date and time when the Amenity instance was created.
    - updated_at: Date and time when the Amenity instance was last updated.
    - name: Name of the amenity.

    Methods:
    - __init__: Initializes a new instance of the Amenity class.

    """

    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the Amenity class.

        Parameters:
        - args: Positional arguments (not used in this implementation).
        - kwargs: Keyword arguments that can be used to initialize the
        instance attributes.

        """

        super().__init__(*args, **kwargs)
        self.name = ""
