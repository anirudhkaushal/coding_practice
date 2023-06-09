from math import *
from collections import *
from sys import *
from os import *

# my approach - brute force with O(n^2) time complexity 
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

# optimal approach - O(n) time complexity using hash maps
def LongestSubsetWithZeroSum_optimal(arr):

    n = len(arr)
    hmap = dict()

    sum = 0
    length = 0

    hmap[sum] = -1

    for i in range(n):
        sum += arr[i]

        if sum in hmap:
            im_length = i - hmap[sum]
            if im_length > length:
                length = im_length
        else:
            hmap[sum] = i

    return length