from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    s = set()
    n = len(arr)

    for i in range(n):
        sum = arr[i]
        count = 1

        if sum == 0:
            s.add(count)

        for j in range(i+1, n):
            sum += arr[j]
            count += 1

            if sum == 0:
                s.add(count)

    if len(s) == 0:
        return 0

    max = float("-inf")
    for v in s:
        if v > max:
            max = v

    return max
