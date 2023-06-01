from os import *
from sys import *
from collections import *
from math import *

# brute force approach: 
# time complexity : almost O(n*m) 
# space complexity: O(m)
def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    
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
        
