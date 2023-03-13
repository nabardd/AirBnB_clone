#!/usr/bin/env python3

import cmd
import json
import re
from shlex import split
import models
from models.base_model import BaseModel
from models.user import User


CLASS_LIST = [
    "BaseModel",
    "User",
]


def check_args(args):
    """
    check args from command line

    Args:
        args (list): command line arguments
    """
    args = args.split(" ")

    if len(args) == 0:
        print("** class name missing **")
    elif args[0] not in CLASS_LIST:
        print("** class doesn't exist **")
    else:
        return (args)


def parse(arg):
    """
    Parse arguments from the command line

    Args:
        arg - list of arguments from the command line
    """
    # regex to check for curly braces
    check_braces = re.search(r"\{(.*?)\}", arg)

    # regex to check for brackets
    check_brackets = re.search(r"\[(.*?)\]", arg)

    if check_braces is None:
        if check_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:check_brackets.span()[0]])
            retl = [i.strip(",") for i in lex]
            retl.append(check_brackets.group())
            return retl
    else:
        lex = split(arg[:check_braces.span()[0]])
        retl = [i.strip(",") for i in lex]
        retl.append(check_braces.group())
        return retl


"""
entry point of the command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
    the entry point of the command interpreter
    """

    prompt = "(hbnb)"
    storage = models.storage

    def do_create(self, argv):
        """
        Creates a new instance of a class <classname>

        Args:
            classname: the name of the class to create
        """

        args = check_args(argv)
        if args:
            print(eval(args[0])().id())
            self.storage.save()

    def do_show(self, argv, id):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save it to the JSON file."""
        args = check_args(argv)
        if args:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(args[0], args[1])
                if instance_id in self.storage.all():
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if args[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[args[2]])
                            setattr(obj, args[2], v_type(args[3]))
                        else:
                            setattr(obj, args[2], args[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_destroy(self, argv):
        """
        Deletes an instance based on the class name and id
        (saves the change to a JSON file)
        """

        args = check_args(argv)

        if args:
            if len(args) != 2:
                print("** no instance found **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in self.storage.all():
                    print("** instance id missing **")
                else:
                    del self.storage.all()[key]
                    self.storage.save()

    def do_all(self, argv):
        """
        Prints all string representation of all instances based on
        the class name
        """

        args = check_args(argv)

        result_list = []

        class_name = args[0]
        for obj, _ in self.storage.all().items():
            if class_name in obj:
                str_rep = f"{obj} {self.storage.all()[obj]}"
                result_list.append(str_rep)

        return (result_list)

    def do_count(self, argv):
        """
        Retrieves the number of instances of a class
        """
        args = check_args(argv)
        class_name = args[0]
        count = 0

        for obj, _ in self.storage.all().items():
            if class_name in obj:
                count += 1

        return (count)

    def do_update(self, argv):
        """
        Updates an instance based on the class name and id
        """
        args = check_args(argv)

        if args:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(args[0], args[1])
                if instance_id in self.storage.all():
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if args[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[args[2]])
                            setattr(obj, args[2], v_type(args[3]))
                        else:
                            setattr(obj, args[2], args[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exits the program"""
        return True

    def emptyline(self):
        """Prevents execution of previous command
        when empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
