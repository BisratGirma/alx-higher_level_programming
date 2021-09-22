#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = -1
    high_key = ""
    for key in a_dictionary:
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
            high_key = key
    return high_key
