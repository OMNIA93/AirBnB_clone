#!/usr/bin/python3
"""
This module contains the HBNBCommand class that implements
the command interpreter.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that implements the command interpreter.

    args:
    prompt: str that will be showed to the user
    classes: Dictionary of available classes

    Methods:
        do_quit(self, arg): Quit command to exit the program
        do_EOF(self, arg): Quit command to exit the program when receive EOF
        emptyline(self): Empty line + ENTER shouldn't execute anythingi
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Place": Place(),
        "Review": Review()
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
