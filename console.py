#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the command line interpreter"""
   
    prompt = '(hbnb) '
    my_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }


    def my_quit(self, arg):
        """Quit command exits the program"""
        return True


    def my_EOF(self, arg):
        """EOF command exits the program"""
        print("")
        return True


    def emptyline(self):
        """an empty line shouldn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
