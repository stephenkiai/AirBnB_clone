#!/usr/bin/env python3

"""
This is the BaseModel module for the AirBnb_clone project.

Module functionality:
- Provides the BaseModel class, which serves as the base
class for other models.
- Handles common attributes and methods for all models.

"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """
    This is the BaseModel class.

    Class functionality:
    - Represents the base class for other models.
    - Handles common attributes and methods for all models.

    Attributes:
    - id: Unique identifier for each instance.
    - created_at: Date and time when the instance was created.
    - updated_at: Date and time when the instance was last updated.

    Methods:
    - __init__: Initializes a new instance of the class.
    - __str__: Returns a string representation of the instance.
    - save: Updates the instance's updated_at attribute and saves
    it to the storage.
    - to_dict: Converts the instance to a dictionary representation.

    """

    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the BaseModel class.

        Parameters:
        - args: Positional arguments (not used in this implementation).
        - kwargs: Keyword arguments that can be used to initialize the
        instance attributes.

        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    if key == 'id':
                        self.id = value
        if not kwargs:
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now()

        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()

    def __str__(self):

        """
            Returns a string representation of the BaseModel instance.

            Returns:
            - A string representation in the format: "[<class name>] (<id>)
            <dictionary representation>"

        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):

        """
        Updates the instance's updated_at attribute and saves it to
        the storage.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        """
        Converts the instance to a dictionary representation.

        Returns:
        - A dictionary containing all the instance's attributes and class name.

        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
