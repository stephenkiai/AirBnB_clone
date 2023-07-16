#!/usr/bin/env python3

"""
This is the test_amenity module for the AirBnb_clone project.

Module functionality:
- Provides the TestAmenity class, which contains unit tests for the Amenity class.

"""

import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    """
        This is the TestAmenity class that contains unit tests for the Amenity class.

        Test cases:
        - test_amenity_attributes: Tests if the Amenity instance has the required attributes.
        - test_amenity_inheritance: Tests if the Amenity instance is an instance of BaseModel.

        """

    def test_amenity_attributes(self):

        """
        Test if the Amenity instance has the required attributes.

        """

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_inheritance(self):

        """
        Test if the Amenity instance is an instance of BaseModel.

        """

        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
    

if __name__ == '__main__':
    unittest.main()
