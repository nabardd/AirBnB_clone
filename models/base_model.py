#!/usr/bin/env python3

import uuid
import os
from datetime import datetime
from . import storage

""" Base Model Class """


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializing the BaseModel class

        Args:

            *args: A list of arguments to pass to initialization
            **kwargs: A dictionary of keyword arguments

        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ('created_at', 'updated_at'):
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints out information on class for which it is requested
        """
        class_name = __class__.__name__

        print(f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the class attribute updated_at with the current datetime
        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()

        return dictionary
