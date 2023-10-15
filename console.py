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
    prompt = "(hbnb) "

    def do_create(self, arg):
        """ Create a new instance of a BaseModel and save it """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Show string representation of an instance """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:  
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance based on the class name and id """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:  # قم بإضافة الفئات الأخرى هنا
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Print all string representations of instances """
        args = arg.split()
        obj_list = []
        if not arg:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if key.split(".")[0] == args[0]:
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """ Update an instance based on the class name and id """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:  
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            if attr_type is str:
                attr_value = str(attr_value)
            elif attr_type is int:
                try:
                    attr_value = int(attr_value)
                except ValueError:
                    pass
            elif attr_type is float:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
            setattr(instance, attr_name, attr_value)
            storage.save()

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        """ Exit the console """
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop(
