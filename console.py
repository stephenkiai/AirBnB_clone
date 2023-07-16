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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
