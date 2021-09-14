#!/usr/bin/python3

"""
a function that prints integer list
"""


def print_list_integer(my_list=[]):
    i = 0
    while i < len(my_list):
        print("{:d}".format(my_list[i]))
        i += 1
