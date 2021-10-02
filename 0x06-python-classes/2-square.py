#!/usr/bin/python3
"""A simple example of defining class.

This class is empty. defined only for example

"""


class Square:
    """This class defines object of square..

    """
    def __init__(self, size=0):
        if size >= 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
