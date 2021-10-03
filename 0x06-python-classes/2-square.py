#!/usr/bin/python3
"""A simple example of defining class.

"""


class Square:
    """This class defines object of square with size.

    Args:
        size (int): the first and only param.

    Raises:
        ValueError: if the size of object is less 0.

    """

    def __init__(self, size=0):
        if size >= 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
