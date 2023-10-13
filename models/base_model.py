#!/usr/bin/python3

import cmd
from datetime import datetime
import json
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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def __str__():
        """
        print class name and id
        """
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()



    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        make_dict = self.__dict__.copy()
        make_dict["__class__"] = self.__class__.__name__
        make_dict["created_at"] = self.created_at.isoformat()
        make_dict["updated_at"] = self.updated_at.isoformat()
        return make_dict
