#!/usr/bin/env python3
"""
- Provides the Review class, which represents a review for an
accommodation place.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Review class.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
