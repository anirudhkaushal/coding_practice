from os import *
from sys import *
from collections import *
from math import *

def inplaceRotate(inputArray, n):

    # trick is to first transpose the matrix and then reverse evry column

    # inplace transpose of the square matrix
    for i in range(n):
        for j in range(i):
            inputArray[i][j], inputArray[j][i] = inputArray[j][i], inputArray[i][j]

    # reversing each column for anti-clockwise 90 deg rotation
    for i in range(n):
        for j in range(n):
             if j < n//2:
                 inputArray[j][i], inputArray[n-1-j][i] = inputArray[n-1-j][i], inputArray[j][i]

    return inputArray
