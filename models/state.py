#!/usr/bin/env python3
"""
- Provides the State class, which represents a state or province.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the State class.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
