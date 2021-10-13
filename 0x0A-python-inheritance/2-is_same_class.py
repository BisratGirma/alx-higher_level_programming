#!/usr/bin/python3
"""Inheritance exercise Module. """


def is_same_class(obj, a_class):
    """Checks if object is instance a class

    Args:
        obj (obj): object
        a_class (class): a class to match with obj

    Return:
        True: if the object is instance of the class
        False: if not.
    """

    if isinstance(obj, bool):
        return a_class is bool
    else:
        return isinstance(obj, a_class)
