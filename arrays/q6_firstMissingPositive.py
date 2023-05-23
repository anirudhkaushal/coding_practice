from os import *
from sys import *
from collections import *
from math import *

# solution using sorting - O(n*logn) & O(1)
def firstMissing(arr, n):

    arr.sort()

    val = 1

    for i in range(n):
        if arr[i] == val:
            val = val + 1        

    return val

# solution using hash set - O(n) & O(n)
def firstMissing_better(arr, n):

    # creating a hash set
    values = set()

    for v in arr:
        if v > 0:
            values.add(v)

    ans = 1

    while ans in values:
        ans += 1

    return ans

# best solution using only one array traversal - O(n) & O(1)
def firstMissing_best(arr, n):

    for i in range(n):
        correctPos = arr[i]-1
        while 1 <= arr[i] <= n and arr[i] != arr[correctPos]:
            arr[i], arr[correctPos] = arr[correctPos], arr[i]
            correctPos = arr[i]-1

    for i in range(n):
        if arr[i] != i+1:
            return i+1

    return n+1


# Main Code
t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing_best(arr,n)

    print(ans)
