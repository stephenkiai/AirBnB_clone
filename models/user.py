#!/usr/bin/env python3
"""
- Provides the User class, which represents a user.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    - Represents a user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
