#!/usr/bin/python3
"""

This function divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number.

    Args:
        matrix: It is a list of lists (matrix)- the members can be ints or floats
        div: The Number to be used for the division.It can be float or an integer
    Raises:
        TypeError: when the matrix contains non-numb
        TypeError: when the matrix contains rows of different sizes
        TypeError: when div is not an int or float
        ZeroDivisionError: when div is 0
    Returns:
        New matrix which represents the result of the divisions
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
