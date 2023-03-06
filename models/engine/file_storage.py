#!/usr/bin/env python3

import json

"""Object representation for file storage"""


class FileStorage:

    """
    Serializes instances to a JSON file and deserializes JSON file
    to instances.
    """

    def __init__(self, file_path="./file.json", objects=dict()):
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
            obj (object): the object to be set in object
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path
        """
        with open(self.__file_path, 'w') as f:
            dict_store = dict()
            for k, v in self.__objects.items():
                dict_store[k] = v.to_dict()
            json.dump(dict_store, f, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path)) exists; otherwise, do nothing. if the file doesn't
        exist, no exception should be raised.
        """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
