#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if (i == row[len(row) - 1]):
                print("{}".format(i))
            else:
                print("{}".format(i), end=" ")
