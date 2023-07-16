#!/usr/bin/python3
""" The AirBnB console"""

import cmd
from models.base_model import BaseModel
from models import storage
import models
import json
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print()
        return True

    def emptyline(self):
        """do nothing for empty line"""
        pass

    def do_create(self, arg):
        """create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """print str repr of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                instance_key = class_name + '.' + args[1]
                if instance_key in instances:
                    print(instances[instance_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """delete instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                instance_key = class_name + '.' + args[1]
                if instance_key in instances:
                    del instances[instance_key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Print all instances or instances of a specific class"""
        classes = storage.classes
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            filtered_instances = [str(value) for key, value in instances.items()
                                  if key.startswith(arg + ".")]
            print(filtered_instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                instance_key = class_name + '.' + args[1]
                if instance_key not in instances:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    instance = instances[instance_key]
                    setattr(instance, attr_name, attr_value)
                    instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
