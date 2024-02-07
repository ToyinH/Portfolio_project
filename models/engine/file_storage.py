#!/usr/bin/python3
"""
Contains the FileStorage class
"""
from models.base_model import BaseModel
import json
from models.user import User
from models.candidate import Candidate
from models.ballot import Ballot
from models.election import Election
from models.result import Result 
from models.vote import Vote 


# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """
        Return a dictionary of instantiated objects in __objects.
        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary
        """
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    cls_dict[key] = value
            return cls_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key, value in FileStorage.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf") as file:
            json.dump(json_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
