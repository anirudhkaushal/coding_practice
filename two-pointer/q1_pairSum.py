from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, n, target):
    
    count = 0

    i = 0
    j = n - 1

    while i < j:
        if arr[i] + arr[j] == target:
            count += 1
            i += 1
            j -= 1
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1

    if count > 0:
        return count

    return -1


