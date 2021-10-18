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
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        raise ValueError("cannot convert float infinity to integer")
    if result == float('nan'):
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)
