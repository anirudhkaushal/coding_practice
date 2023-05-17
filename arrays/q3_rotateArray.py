# rotate array problem

from os import *
from sys import *
from collections import *
from math import *


def rotateArray(n, arr, k):

    for i in range(k):
        val = arr.pop(0)
        arr.append(val)

    return arr



n = int(input())
arr_str = input()
arr_vals = arr_str.split()
arr = []

for i in range(n):
    arr.append(int(arr_vals[i]))

k = int(input())

res = rotateArray(n, arr, k)

for val in res:
    print(val, end = " ")



