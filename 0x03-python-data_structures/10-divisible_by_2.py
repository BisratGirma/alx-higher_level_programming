#!/usr/bin/python3

'''
finds all multiples of 2 in a list
'''


def divisible_by_2(my_list=[]):
    new_list = [False] * len(my_list)
    for idx, num in enumerate(my_list):
        if num % 2 == 0:
            new_list[idx] = True
    return new_list
