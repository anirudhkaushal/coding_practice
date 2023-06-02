# Finding the maximum sub-array sum

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

# brute force approach
# time complexity - O(n^2)
# space complexity - O(1) 
def maxSubarraySum_(arr, n):

    if n == 0:
        return 0

    max_sum = 0

    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j]
            max_sum = max(max_sum, sum_)

    return max_sum


# optimal approach - using Kadane's algorithm
# time complexity - O(n)
# space complexity - O(1)
def maxSubarraySum(arr, n):

    if n == 0:
        return 0

    max_sum = 0
    curr_sum = 0

    for i in range(n):

        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
