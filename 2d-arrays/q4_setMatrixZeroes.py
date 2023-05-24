from math import *
from collections import *
from sys import *
from os import *

from typing import List

# my initial approach (incorrect; i am taking extra space)
# here i am storing the index of rows and columns which have zeroes and then traversing the matrix again and placing 0s based on row and col index
# however, i am using extra space and the question asks this to be done 'in place'
def setZeros_1(matrix: List[List[int]]) -> None:
	
    n = len(matrix)
    m = len(matrix[0])

    row_idx = []
    col_idx = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row_idx.append(i)
                col_idx.append(j)

    for i in range(n):
        for j in range(m):
            if i in row_idx or j in col_idx:
                matrix[i][j] = 0

# in place brute force approach
# initially, traverse whole matrix and whenever there is a 0, set the respective row and col to be equal to -1 
# now this will work if we are sure that input matrix has no negative elements

                
