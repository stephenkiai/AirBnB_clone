#!/usr/bin/python3
""" The AirBnB console"""

from models.base_model import BaseModel
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re



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
    
    def do_create(self, args):
        """
        Create a new instance of a given class.
        Usage: create <class name> [param1=value1] [param2=value2] ...
        """
        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        class_name = parts[0]
        model_class = self.classes.get(class_name)
        if not model_class:
            print("** class doesn't exist **")
            return

        new_instance = model_class()
        for part in parts[1:]:
            key, value = part.split('=')
            value = value.strip('"')
            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Show an object based on class and UUID.
        Usage: show <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name = parts[0]
        instance_id = parts[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        print(all_objs[key])
    
    def do_destroy(self, args):
        """
        Destroy an object based on class and UUID.
        Usage: destroy <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name = parts[0]
        model_class = self.classes.get(class_name)
        if not model_class:
            print("** class doesn't exist **")
            return

        instance_id = parts[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        del all_objs[key]
        storage.save()
    
    def do_all(self, args):
        """
        Show all objects or all objects of a given class.
        Usage: all [class name]
        """
        parts = args.split()
        if parts:
            class_name = parts[0]
            model_class = self.classes.get(class_name)
            if model_class:
                if hasattr(model_class, 'all'):
                    objects = model_class.all()
                else:
                    objects = storage.all()
                    objects = [obj for obj in objects.values() if isinstance(obj, model_class)]
            else:
                print("** class doesn't exist **")
                return
        else:
            objects = storage.all()

        filtered_objects = [str(obj) for obj in objects]
        print(filtered_objects)

    def do_update(self, args):
        """
        Update existing attributes of an object based on class name and UUID.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name = parts[0]
        model_class = self.classes.get(class_name)
        if not model_class:
            print("** class doesn't exist **")
            return

        instance_id = parts[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(parts) < 4:
            print("** attribute name missing **")
            return

        attribute_name = parts[2]
        attribute_value = parts[3]

        instance = all_objs[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, args):
        """
        Count the number of instances of a class.
        Usage: <class name>.count()
        """
        class_name = args.strip().split('.')[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        count = sum(1 for obj in objects.values() if type(obj).__name__ == class_name)
        print(count)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
