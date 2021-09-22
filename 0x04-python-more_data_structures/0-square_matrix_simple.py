#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new = [[n * n for n in x] for x in matrix]
    return new
