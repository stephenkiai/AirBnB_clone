#!/usr/bin/env python3
"""
- Provides the City class, which represents a city for
accommodations.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    - Represents a city for accommodations.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
