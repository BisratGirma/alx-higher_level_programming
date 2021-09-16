#!/usr/bin/python3

'''
returns a tuple with the length of a string and its first character
'''


def multiple_returns(sentence):
    t = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return t
