from os import *
from sys import *
from collections import *
from math import *

# brute force approach: 
# time complexity : almost O(n*m) 
# space complexity: O(m)
def findArrayIntersection_(arr: list, n: int, brr: list, m: int):
    
    vis = [0]*m
    ans = []

    for i in range(n):
        for j in range(m):

            if arr[i] == brr[j] and vis[j] == 0:
                ans.append(arr[i])
                vis[j] = 1
                break

            if arr[i] < brr[j]:
                break

    return ans
        
# optimal approach
# time complexity: in worst case O(n + m)
# space complexity: O(1)
def findArrayIntersection(arr: list, n: int, brr: list, m: int):

    i = 0
    j = 0
    ans = []

    while i < n and j < m:
        if arr[i] < brr[j]:
            i += 1
        elif arr[i] > brr[j]:
            j += 1
        else:
            ans.append(arr[i])
            i += 1
            j += 1

    return ans


