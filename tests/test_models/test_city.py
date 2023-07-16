#!/usr/bin/env python3
"""
This is the test_city module for the AirBnb_clone project.

Module functionality:
- Provides the TestCity class, which contains unit tests for the City class.

"""
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    This is the TestCity class that contains unit tests for the City class.

    Test cases:
    - setUp: Sets up the test fixture.
    - test_city_inherits_from_base_model: Tests if the City instance inherits from BaseModel.
    - test_city_attributes: Tests if the City instance has the required attributes.
    - test_city_to_dict: Tests if the to_dict method returns the correct dictionary representation.
    - test_city_str_representation: Tests if the __str__ method returns the correct string representation.
    - test_city_update_attributes: Tests if the City instance allows attribute updates.
    - test_city_save_updates_timestamp: Tests if the save method updates the timestamp.

    """
    def setUp(self):
        """
        Sets up the test fixture.

        """
        self.city = City()

    def test_city_inherits_from_base_model(self):
        """
        Test if the City instance inherits from BaseModel.

        """
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        """
        Test if the City instance has the required attributes.

        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_to_dict(self):
        """
        Test if the to_dict method returns the correct dictionary representation.

        """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["state_id"], "")
        self.assertEqual(city_dict["name"], "")

    def test_city_str_representation(self):
        """
        Test if the __str__ method returns the correct string representation.

        """
        city_str = str(self.city)
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(city_str, expected_str)

    def test_city_update_attributes(self):
        """
        Test if the City instance allows attribute updates.

        """
        self.city.state_id = "state_123"
        self.city.name = "New York"
        self.assertEqual(self.city.state_id, "state_123")
        self.assertEqual(self.city.name, "New York")

    def test_city_save_updates_timestamp(self):
        """
        Test if the save method updates the timestamp.

        """
        previous_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, previous_updated_at)

   

if __name__ == '__main__':
    unittest.main()
