#!/usr/bin/python3

import cmd
import datetime
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
        self.name = "BaseModel"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at


    def __str__():
        """
        print class name and id
        """
        print(f"[{}] ({}) {}", self.name, self.id, self.__dict__)


    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()



    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        pass
