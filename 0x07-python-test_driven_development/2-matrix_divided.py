#!/usr/bin/python3
"""Defining a matrix division function"""


def matrix_divided(matrix, div):
    """
    function that will divide all the elements in the matrex

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError:if matrix not list of lists of intgers/float
        TypeError:if row inmatrix not same size
        TypeError:if div not intger of float
        ZeroDivisionError: if div == 0
    Retruns:
        will return new matrix that will have the result after the divistion
    """

    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for r in matrix:
        new_row = []
        for Element_row in r:
            new_row.append(round(Element_row / div, 2))
        new_matrix.append(new_row)

    return new_matrix
