#!usr/bin/env python3
"""
This module contains the unit tests for the console.py module.
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test cases for the Console class.
    """
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        pass

    def test_prompt(self):
        """Test the prompt property of the Console class."""
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_emptyline(self):
        """Test the behavior of an empty line input."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("")
            self.assertEqual("", mock_stdout.getvalue())

    def test_quit(self):
            """Test the 'quit' command."""
            self.console.onecmd("quit")

    def test_create_missing_class_name(self):
        """Test behavior when the class name is missing for the 'create' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    def test_create_invalid_class_name(self):
        """Test behavior when an invalid class name is provided for the 'create' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_create(self, mock_storage):
        """Test the 'create' command."""
        mock_storage.all.return_value = {}
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue()
            self.assertIsNotNone(output)
            self.assertEqual(len(output.strip()), 36)  # UUID format

    def test_show_missing_class_name(self):
        """Test behavior when the class name is missing for the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    def test_show_missing_instance_id(self):
        """Test behavior when the instance id is missing for the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

    def test_show_invalid_class_name(self):
        """Test behavior when an invalid class name is provided for the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show MyModel 123")
            self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_show_nonexistent_instance(self, mock_storage):
        """Test behavior when the instance does not exist for the 'show' command."""
        mock_storage.all.return_value = {}
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel 123")
            self.assertEqual("** no instance found **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_show(self, mock_storage):
        """Test the 'show' command."""
        instance_id = "123"
        mock_instance = MagicMock()
        mock_instance.__str__.return_value = f"MockInstance {instance_id}"
        mock_storage.all.return_value = {
            "BaseModel.123": mock_instance
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd(f"show BaseModel {instance_id}")
            

    def test_destroy_missing_class_name(self):
        """Test behavior when the class name is missing for the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    def test_destroy_missing_instance_id(self):
        """Test behavior when the instance id is missing for the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

    def test_destroy_invalid_class_name(self):
        """Test behavior when an invalid class name is provided for the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy MyModel 123")
            self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_destroy_nonexistent_instance(self, mock_storage):
        """Test behavior when the instance does not exist for the 'destroy' command."""
        mock_storage.all.return_value = {}
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel 123")
            self.assertEqual("** no instance found **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_destroy(self, mock_storage):
        """Test the 'destroy' command."""
        instance_id = "123"
        mock_instance = MagicMock()
        mock_storage.all.return_value = {
            "BaseModel.123": mock_instance
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd(f"destroy BaseModel {instance_id}")
            
            

    def test_all_invalid_class_name(self):
        """Test behavior when an invalid class name is provided for the 'all' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_all(self, mock_storage):
        """Test the 'all' command."""
        mock_instance1 = MagicMock()
        mock_instance1.__str__.return_value = "MockInstance1"
        mock_instance2 = MagicMock()
        mock_instance2.__str__.return_value = "MockInstance2"
        mock_storage.all.return_value = {
            "BaseModel.123": mock_instance1,
            "BaseModel.456": mock_instance2
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all")
            
    def test_update_missing_class_name(self):
        """Test behavior when the class name is missing for the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    def test_update_missing_instance_id(self):
        """Test behavior when the instance id is missing for the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

    def test_update_invalid_class_name(self):
        """Test behavior when an invalid class name is provided for the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update MyModel 123")
            self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_update_nonexistent_instance(self, mock_storage):
        """Test behavior when the instance does not exist for the 'update' command."""
        mock_storage.all.return_value = {}
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel 123")
            self.assertEqual("** no instance found **\n", mock_stdout.getvalue())

    @patch('models.storage')
    def test_update_missing_attribute_name(self, mock_storage):
        """Test behavior when the attribute name is missing for the 'update' command."""
        instance_id = "123"
        mock_instance = MagicMock()
        mock_storage.all.return_value = {
            "BaseModel.123": mock_instance
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd(f"update BaseModel {instance_id}")
            

    @patch('models.storage')
    def test_update(self, mock_storage):
        """Test the 'update' command."""
        instance_id = "123"
        attribute_name = "name"
        attribute_value = "John"
        mock_instance = MagicMock()
        mock_storage.all.return_value = {
            "BaseModel.123": mock_instance
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd(f"update BaseModel {instance_id} {attribute_name} '{attribute_value}'")
            setattr(mock_instance, attribute_name, attribute_value)
            


if __name__ == '__main__':
    unittest.main()