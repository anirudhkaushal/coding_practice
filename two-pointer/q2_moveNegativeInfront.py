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



