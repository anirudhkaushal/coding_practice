from os import *
from sys import *
from collections import *
from math import *

from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

