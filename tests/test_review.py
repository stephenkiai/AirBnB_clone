#!/usr/bin/env python3
"""
This is the test_review module for the AirBnb_clone project.

Module functionality:
- Provides the TestReview class, which contains unit tests
for the Review class.

"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    This is the TestReview class that contains unit tests for the Review class.
    """
    def test_review_attributes(self):
        """
        Test if the Review instance has the required attributes.

        """
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_inheritance(self):
        """
        Test if the Review instance inherits from BaseModel.

        """
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == '__main__':
    unittest.main()
