#!/usr/bin/env python3
"""
This is the test_user module for the AirBnb_clone project.

Module functionality:
- Provides the TestUser class, which contains unit tests for the User class.

"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This is the TestUser class that contains unit tests for the User class.
    """
    def test_user_attributes(self):
        """
        Test if the User instance has the required attributes.

        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_inheritance(self):
        """
        Test if the User instance inherits from BaseModel.

        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_initialization(self):
        """
        Test if the User instance is initialized correctly.

        """
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_to_dict(self):
        """
        Test if the to_dict method returns the correct dictionary
        representation.

        """
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
