#!/usr/bin/python3
"""Defines My List class."""


class MyList(list):
    """
    A class MyList that inherits from list.
    Provides a method to print the list in sorted ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted ascending order.
        Assumes all elements are of type int.
        """
        print(sorted(self))
