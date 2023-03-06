#!/usr/bin/env python3

import cmd

"""
entry point of the command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
    the entry point of the command interpreter
    """

    prompt = "(hbnb)"

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
