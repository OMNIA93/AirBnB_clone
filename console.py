#!/usr/bin/python3
"""
This module contains the HBNBCommand class that implements
the command interpreter.
"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage
class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that implements the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program when receiving EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance based on class name and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_instances = storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in all_instances:
            print(all_instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id (save the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_instances = storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in all_instances:
            del all_instances[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances based or not on the class name.
        """
        args = arg.split()
        all_instances = storage.all()
        if not arg:
            print([str(val) for val in all_instances.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(val) for key, val in all_instances.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """
        Update an instance based on class name and id by adding or updating attribute.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        all_instances = storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in all_instances:
            instance = all_instances[instance_key]
            attr_name = args[2]
            attr_value = args[3]
            # Update the attribute based on its type (string, integer, or float)
            if attr_value[0] == '"' and attr_value[-1] == '"':
                attr_value = attr_value[1:-1]
            elif "." in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
