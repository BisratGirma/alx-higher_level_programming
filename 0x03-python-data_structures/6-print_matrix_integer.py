#!/usr/bin/python3

'''
print only matrix integers
'''


def print_matrix_integer(matrix=[[]]):
    for e in matrix:
        for i in e:
            print('{:d}'.format(i), end='')
            if i != e[-1]:
                print(' ', end='')
        print("")
