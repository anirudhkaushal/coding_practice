from os import *
from sys import *
from collections import *
from math import *

def coverageOfMatrix(mat):
    
    n = len(mat)
    m = len(mat[0])

    count = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                    if i-1 >= 0 and mat[i-1][j] == 1:
                        count += 1

                    if i+1 < n and mat[i+1][j] == 1:
                        count += 1

                    if j-1 >= 0 and mat[i][j-1] == 1:
                        count += 1

                    if j+1 < m and mat[i][j+1] == 1:
                        count += 1

    return count

