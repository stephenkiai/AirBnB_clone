#!/usr/bin/env python3
"""
This is the test_state module for the AirBnb_clone project.

Module functionality:
- Provides the TestState class, which contains unit tests for the State class.

"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """
    This is the TestState class that contains unit tests for the State class.

    Test cases:
    - test_state_attributes: Tests if the State instance has the required attributes.
    - test_state_inheritance: Tests if the State instance inherits from BaseModel.

    """
    def test_state_attributes(self):
        """
        Test if the State instance has the required attributes.

        """
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_state_inheritance(self):
        """
        Test if the State instance inherits from BaseModel.

        """
        state = State()
        self.assertIsInstance(state, BaseModel)
    

if __name__ == '__main__':
    unittest.main()
