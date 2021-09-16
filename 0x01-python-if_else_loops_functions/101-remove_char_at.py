#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    i = 0
    for c in str:
        if i != n:
            ch += c
        i += 1
    return ch
