#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.____name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    cls_name, obj_id = key.split(".")
                    obj = models.classes[cls_name](**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
