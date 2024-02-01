#!/usr/bin/python3
"""
a class BaseModel that defines
all common attributes/methods for other classes
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    The BaseModel class that defines all common methods
    and attributes for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        class constructor for BaseModel
        Args:
            args: list of arguments
            kwargs: keyword arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        the __str__ method
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """
        method that updates the public attribut update_at and save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Public instance method that returns a dictionary
        containing all keys/values of __dict__ of the instance

        Returns:
            return the dictionary of __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
