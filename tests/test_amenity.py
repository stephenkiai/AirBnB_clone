#!/usr/bin/env python3
"""
- Provides the TestAmenity class, which contains unit tests for
the Amenity class.
"""
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
        This is the TestAmenity class that contains unit tests for
        the Amenity class.
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
