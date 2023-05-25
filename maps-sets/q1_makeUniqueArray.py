from os import *
from sys import *
from collections import *
from math import *



def minElementsToRemove(arr):

    freq = dict()

    for val in arr:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    count = 0
    for y in freq.values():
        if y > 1:
            count += (y-1)

    return count
