#!/usr/bin/python3
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        sys.exit(0)

    def emptyline(self):
        """Called when an empty line is entered"""
        pass
<<<<<<< HEAD

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        args = shlex.split(arg)
=======
    

    def precmd(self, line):

        """
            Preprocess the command line input before execution.

            This method is called before the execution of each command.
            It processes the command line input and performs any
            necessary transformations.

            Parameters:
            - line: The command line input string.

            Returns:
            - The modified command line input string.

            """
        command_pattern = r"^(?P<command>[a-zA-Z]+)(\((?P<args>.*)\))?$"
        class_command_pattern = r"^(?P<class>[a-zA-Z]+)\.(?P<command>[a-zA-Z_]+)\(\)$"
        class_show_pattern = r"^(?P<class>[a-zA-Z]+)\.show\((?P<id>.*)\)$"
        class_destroy_pattern = r"^(?P<class>[a-zA-Z]+)\.destroy\((?P<id>.*)\)$"
        match_command = re.match(command_pattern, line)
        match_class_command = re.match(class_command_pattern, line)
        match_class_show = re.match(class_show_pattern, line)
        match_class_destroy = re.match(class_destroy_pattern, line)

        if match_command:
            command = match_command.group("command")
            args = match_command.group("args")
            if command in self.dot_cmds:
                if args:
                    args = args.split(", ")
                else:
                    args = []
                args.insert(0, command)
                return " ".join(args)

        elif match_class_command:
            class_name = match_class_command.group("class")
            command = match_class_command.group("command")
            model_class = self.classes.get(class_name)
            if not model_class:
                print("** class doesn't exist **")
                return
            return f"{command} {class_name}"

        elif match_class_show:
            class_name = match_class_show.group("class")
            instance_id = match_class_show.group("id")
            model_class = self.classes.get(class_name)
            if not model_class:
                print("** class doesn't exist **")
                return
            return f"show {class_name} {instance_id}"
        elif match_class_destroy:
            class_name = match_class_destroy.group("class")
            instance_id = match_class_destroy.group("id")
            model_class = self.classes.get(class_name)
            if not model_class:
                print("** class doesn't exist **")
                return
            return f"destroy {class_name} {instance_id}"

        return line
    
    def do_create(self, args):
        """
        Create a new instance of a given class.
        Usage: create <class name> [param1=value1] [param2=value2] ...
        """
>>>>>>> 45ab58987fb553b5c03e0360c120b4b506284541
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            instance = storage.classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances or instances of a specific class"""
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            filtered_instances = [str(value) for key, value in instances.items() if key.startswith(arg + ".")]
            print(filtered_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                instance = storage.all()[key]
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    if hasattr(instance, attr_name):
                        attr_type = type(getattr(instance, attr_name))
                        try:
                            attr_value = attr_type(attr_value)
                            setattr(instance, attr_name, attr_value)
                            instance.save()
                        except ValueError:
                            print("** invalid value type **")
                    else:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_help(self, arg):
        """Help command to display information about commands"""
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
