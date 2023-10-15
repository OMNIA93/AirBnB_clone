#!/usr/bin/python3

import json
<<<<<<< HEAD
=======

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3a82300689e2682a62098115116c12a9787ffbee
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

<<<<<<< HEAD
 =======
>>>>>>> 7d4dc8f5f43dc65225c4ca9c0e37d931e3e17ce0

<<<<<<< HEAD

=======
>>>>>>> 810e85ef570ab3e5360ad3c381153171476c5b6a
>>>>>>> 3a82300689e2682a62098115116c12a9787ffbee
class FileStorage:
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
