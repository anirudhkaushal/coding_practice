from math import *
from collections import *
from sys import *
from os import *

from typing import List

# my initial approach (incorrect; i am taking extra space)
# here i am storing the index of rows and columns which have zeroes and then traversing the matrix again and placing 0s based on row and col index
# however, i am using extra space and the question asks this to be done 'in place'
# time complexity: O(n * m) * O(n + m)  [second part comes from searching; see line 29]
# space complexity: O(n + m) [for storing the row and column indexes]
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
# time complexity: O(n * m) + O(n + m)
# space complexity: O(1)
def setZeros_2(matrix: List[List[int]]) -> None:
	
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:

                for k in range(m):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1

                for h in range(n):
                    if matrix[h][j] != 0:
                        matrix[h][j] = -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

                
# constant space better approach
# here, we keep an extra row and extra col of size m and n resp. (make them empty lists)
# we first traverse the matrix and whenever there is a 0, we place 0 in the corresponding row_ext and col_ext index 
# we then traverse the matrix once again and for each element we check if there is a 0 in any of the row_ext and col_ext corresponding index; if yes, then we mark the current element as 0
# time complexity: O(n*m) 
# space complexity: O(n + m) // constant space
def setZeros_3(matrix: List[List[int]]) -> None:
	
    n = len(matrix)
    m = len(matrix[0])

    row_ext = [None] * m
    col_ext = [None] * n

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row_ext[j] = 0
                col_ext[i] = 0

    for i in range(n):
        for j in range(m):
            if col_ext[i] == 0 or row_ext[j] == 0:
                matrix[i][j] = 0