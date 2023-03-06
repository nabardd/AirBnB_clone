#!/usr/bin/env python3

import uuid
import os
import datetime

""" Base Model Class """


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self) -> None:
        """
        Initializing the Base class

        Args:

        """
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

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
        self.update_at = datetime.datetime.now()

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
