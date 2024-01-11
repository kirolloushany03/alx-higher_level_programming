#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_new_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        my_new_matrix.append(result)
    return my_new_matrix
