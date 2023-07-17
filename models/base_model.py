#!/usr/bin/env python3

"""
- Provides the BaseModel class, which serves as the base
class for other models.
- Handles common attributes and methods for all models.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    - Represents the base class for other models.
    - Handles common attributes and methods for all models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
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
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
