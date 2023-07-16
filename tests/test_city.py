#!/usr/bin/env python3
"""
This is the test_city module for the AirBnb_clone project.

Module functionality:
- Provides the TestCity class, which contains unit tests for
the City class.

"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    TestCity class that contains unit tests for the City class.
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
        Test if to_dict method returns correct dictionary representation.

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
