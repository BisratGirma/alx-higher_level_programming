#!/usr/bin/python3

'''
deletes c's from string
'''


def no_c(my_string):
    copy_str = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(copy_str))
