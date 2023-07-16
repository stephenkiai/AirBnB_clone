#!/usr/bin/env python3

"""
This is the User module for the AirBnb_clone project.

Module functionality:
- Provides the User class, which represents a user.
- Inherits from the BaseModel class.

"""

from models.base_model import BaseModel


class User(BaseModel):

    """
    This is the User class that inherits from BaseModel.

    Class functionality:
    - Represents a user.

    Attributes:
    - id: Unique identifier for each User instance.
    - created_at: Date and time when the User instance was created.
    - updated_at: Date and time when the User instance was last updated.
    - email: Email address of the user.
    - password: Password of the user.
    - first_name: First name of the user.
    - last_name: Last name of the user.

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
