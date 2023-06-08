from os import *
from sys import *
from collections import *
from math import *

def findKthElement(mat, k):

    # Write your code here
    # Return k'th element in spiral form of matrix

    n = len(mat)
    m = len(mat[0])

    left = 0
    top = 0
    right = m - 1
    bottom = n - 1

    count = 0

    while top <= bottom and left <= right:

        for i in range(left, right+1):
            count += 1

            if count == k:
                return mat[top][i]
        top += 1

        for i in range(top, bottom+1):
            count += 1

            if count == k:
                return mat[i][right]
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                count += 1

                if count == k:
                    return mat[bottom][i]
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                count += 1

                if count == k:
                    return mat[i][left]
            left += 1
