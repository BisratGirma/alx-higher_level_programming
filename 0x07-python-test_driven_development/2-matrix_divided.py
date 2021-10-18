#!/usr/bin/python3
"""A module on test driven development """

def matrix_divided(matrix, div):
    new_matrix = matrix 
    for raws in new_matrix:
        for element in raws:
            element = element / div
    return new_matrix
