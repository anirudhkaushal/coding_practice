from os import *
from sys import *
from collections import *
from math import *

from typing import List


def sort(n: int, arr: List[int]) -> List[int]:
    # writw your code here
    
    max_el = max(arr)
    min_el = min(arr)

    r = (max_el - min_el) + 1

    store = [0]*r

    for a in arr:
        store[a - min_el] += 1

    ans = []
    for i in range(r):
        cnt = store[i]

        for j in range(cnt):
            ans.append(i + min_el)

    return ans
