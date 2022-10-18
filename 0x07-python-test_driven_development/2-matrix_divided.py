#!/usr/bin/python3
"""a fuction that divide the elements in a list"""


def matrix_divided(matrix, div):
    """
    A function that divide a list by a nmber
    checking the case for wrong inpt or type
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    size = 1
    for elements in matrix:
        if type(elements) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
        for values in elements:
            if type(values) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")
        if (size == 1):
            size = len(elements)
        elif (size != len(elements)):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return ([[round(values/div, 2) for values in elements]
            for elements in matrix])
