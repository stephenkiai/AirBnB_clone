#!/usr/bin/env python3
"""
- Provides the TestBaseModel class, which contains unit tests for the
BaseModel class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        This is the TestBaseModel class that contains unit tests for the
        BaseModel class.
        """
    def test_initialization(self):
        """
        Test if the BaseModel instance is initialized correctly.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict(self):
        """
        Test if to_dict method returns correct dictionary representation.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str_representation(self):
        """
        Test if the __str__ method returns the correct string representation.
        """
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_attribute_assignment(self):
        """
        Test if the instance allows attribute assignment.
        """
        obj = BaseModel()
        obj.name = "John"
        self.assertTrue(hasattr(obj, 'name'))
        self.assertEqual(obj.name, "John")

    def test_attribute_reassignment(self):
        """
        Test if the instance allows attribute reassignment.
        """
        obj = BaseModel()
        obj.name = "John"
        obj.name = "Jane"
        self.assertEqual(obj.name, "Jane")

    def test_attribute_removal(self):
        """
        Test if the instance allows attribute removal.
        """
        obj = BaseModel()
        obj.name = "John"
        del obj.name
        self.assertFalse(hasattr(obj, 'name'))

    def test_save_updates_updated_at(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict_includes_custom_attributes(self):
        """
        Test if the to_dict method includes custom attributes.
        """
        obj = BaseModel()
        obj.custom_attribute = 'custom_value'
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['custom_attribute'], 'custom_value')

    def test_id_uniqueness(self):
        """
        Test if the generated IDs are unique.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_initialization_with_kwargs(self):
        """Test if the BaseModel instance is initialized correctly with kwargs."""
        kwargs = {
            'id': '123',
            'created_at': '2023-07-01T12:00:00.000000',
            'updated_at': '2023-07-01T12:00:00.000000',
            'custom_attribute': 'custom_value'
        }
        obj = BaseModel(**kwargs)
        self.assertIsInstance(obj, BaseModel)

    def test_initialization_without_kwargs(self):
        """Test if the BaseModel instance is initialized correctly without kwargs."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_representation(self):
        """Test if the __str__ method returns the correct string representation."""
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute."""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns correct dictionary representation."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
        self.assertNotIn('custom_attribute', obj_dict)  # Custom attribute should not be in the dict

    def test_id_uniqueness(self):
        """Test if the generated IDs are unique."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_custom_attribute_assignment(self):
        """Test if the instance allows assignment of a custom attribute."""
        obj = BaseModel()
        obj.custom_attribute = 'custom_value'
        self.assertTrue(hasattr(obj, 'custom_attribute'))
        self.assertEqual(obj.custom_attribute, 'custom_value')

    def test_custom_attribute_reassignment(self):
        """Test if the instance allows reassignment of a custom attribute."""
        obj = BaseModel()
        obj.custom_attribute = 'custom_value'
        obj.custom_attribute = 'new_value'
        self.assertEqual(obj.custom_attribute, 'new_value')

    def test_custom_attribute_removal(self):
        """Test if the instance allows removal of a custom attribute."""
        obj = BaseModel()
        obj.custom_attribute = 'custom_value'
        del obj.custom_attribute
        self.assertFalse(hasattr(obj, 'custom_attribute'))


if __name__ == '__main__':
    unittest.main()
