#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if replace is None:
        return my_list
    new = [i for i in my_list]
    for i, v in enumerate(my_list):
        if v == search:
            new[i] = replace
    return new
