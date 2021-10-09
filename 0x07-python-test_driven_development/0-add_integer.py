#!/usr/bin/python3
"""Adding Two values. """


def add_integer(a, b=98):
    """This functions addes two integers
    Args:
        a (int): first integer value.
        b (int): second integer value.

    Return:
        The sum of the arguments

    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    b = int(b)
    if a is None or type(a) is not int:
        raise TypeError("a must be an integer")
    if b is None or type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
