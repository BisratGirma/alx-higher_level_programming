#!/usr/bin/python3

'''
dont copy the address of the old list
'''

def new_in_list(my_list, idx, element):
    if my_list is None:
        pass
    elif idx < 0 and idx >= len(my_list):
        return my_list
    else:
        new_list=list(my_list)
        new_list[idx]=element
        return new_list
