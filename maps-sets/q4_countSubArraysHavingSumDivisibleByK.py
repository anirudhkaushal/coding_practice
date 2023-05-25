from os import *
from sys import *
from collections import *
from math import *

# my approach - brute force with O(n^2) time complexity (did not get accepted - time limit exceeded)
def subArrayCount(arr, k):

    # s = set()
    n = len(arr)
    count = 0

    for i in range(n):
        sum = arr[i]

        if sum % k == 0:
            count += 1

        for j in range(i+1, n):
            sum += arr[j]

            if sum % k == 0:
                count += 1

    return count
