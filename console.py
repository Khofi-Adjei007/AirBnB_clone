#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd  # Importing the cmd module for creating a command-line interpreter
import re   # Importing the re module for regular expression matching
import json  # Importing the json module for JSON parsing and manipulation
from models import storage  # Importing the storage module for data storage
from models.base_model import BaseModel  # Importing the BaseModel class


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "  # Setting the command prompt

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # ...
        # This method seems to handle parsing and
        # executing custom commands.
        # It extracts class name, method, arguments,
        # and attributes from the command string.

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        # ...
        # This method seems to handle updating instances
        # using a dictionary of attributes.

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()  # Print a newline for visual clarity
        return True
        # Return True to exit the command loop (EOF signals program end)

    def do_quit(self, line):
        """Exits the program."""
        return True  # Return True to exit the command loop

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass  # Do nothing when an empty line is entered

    def do_create(self, line):
        """Creates an instance."""
        # ...
        # This method seems to create instances of specified classes.

    def do_show(self, line):
        """Prints the string representation of an instance."""
        # ...
        # This method seems to print the string
        # representation of instances based on their IDs.

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        # ...
        # This method seems to delete instances based on class name and ID.

    def do_all(self, line):
        """Prints all string representation of all instances."""
        # ...
        # This method seems to print string representations of
        # all instances or instances of a specific class.

    def do_count(self, line):
        """Counts the instances of a class."""
        # ...
        # This method seems to count instances of a specified class.

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        # ...
        # This method seems to update instance attributes.


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    # Instantiate the HBNBCommand class and start the command loop
