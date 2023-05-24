from os import *
from sys import *
from collections import *
from math import *

def isMatrixSymmetric(matrix):

    n = len(matrix)

    # matrix2 = []

    # for i in range(n):
    #     row = []
    #     for j in range(n):
    #         row.append(matrix[j][i])
    #     matrix2.append(row)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True
