def add_integer(a, b=98):
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    b = int(b)
    if type(a) is not int:
        raise TypeError("{} must be an integer".format(a))
    if type(b) is not int:
        raise TypeError("{} must be an integer".format(b))
    return a + b
