#!/usr/bin/env python3
"""
- Provides the FileStorage class, which manages the storage of objects in a JSON file.
"""
import json
import uuid
from os.path import exists


class FileStorage:
    """
    - __file_path: The path to the JSON file where objects are stored.
    - __objects: A dictionary that stores objects as key-value pairs.
    - classes: A dictionary that stores class names as keys and their corresponding class objects as values.
    """
    __file_path = "file.json"
    __objects = {}
    classes = {}
    
    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets obj with key <obj class name>.id in __objects"""
        if not hasattr(obj, "id"):
            setattr(obj, "id", str(uuid.uuid4()))
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the json file(path:__file_path)"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """if file exist deserialize json file to __objects else do nothing"""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            from models.base_model import BaseModel
            
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj = BaseModel(**value)
                self.__objects[key] = obj
