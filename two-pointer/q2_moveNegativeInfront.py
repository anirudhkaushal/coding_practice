from os import *
from sys import *
from collections import *
from math import *

# my approach - approx O(n^2) time complexity - bubble sort like approach
def separateNegativeAndPositive(nums):

    j = 0
    i = 0

    while i < len(nums):

        if nums[i] < 0:
            j = i
            while j > 0 and nums[j-1] >= 0:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1

        i += 1

    return nums

# two pointer approach - one pointer at first element; other pointer at last element
def separateNegativeAndPositive_(nums):

    n = len(nums)
    i = 0
    j = n - 1

    while i < j:

        if nums[i] < 0 and nums[j] >= 0:
            i += 1
            j -= 1
        elif nums[i] >= 0 and nums[j] < 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[i] < 0 and nums[j] < 0:
            i += 1
        else:
            j -= 1

    return nums 

# partition approach - which is used in quick sort
def separateNegativeAndPositive__(nums):

    n = len(nums)
    i = -1
    pivot = 0

    for j in range(n):

        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    return nums
            








