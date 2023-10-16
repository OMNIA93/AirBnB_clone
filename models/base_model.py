#!/usr/bin/python3
""" module for BaseModel class """

import cmd
from datetime import datetime
from models import storage
import json
import os
import sys
import uuid


class BaseModel():
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        method to take inistance from basemodel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or k == "updated_at":
                   setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                     setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        print class name and id
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        _dict__ of the instance
        """
        make_dict = self.__dict__.copy()
        make_dict["__class__"] = self.__class__.__name__
        make_dict["created_at"] = self.created_at.isoformat()
        make_dict["updated_at"] = self.updated_at.isoformat()
        return make_dict
