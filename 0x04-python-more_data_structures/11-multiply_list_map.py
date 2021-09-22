#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        return
    new = [v * number for v in my_list]
    return new
