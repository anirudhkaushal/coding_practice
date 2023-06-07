from math import *
from collections import *
from sys import *
from os import *

# my approach - using hashmap/dictionary
# here, we have 2 iterations - one of the arr, and other of the hashmap
def majorityElementII__(arr):
	# Write your code here.
	
	n = len(arr)
	mpp = {}

	for a in arr:
		if a in mpp:
			mpp[a] += 1
		else:
			mpp[a] = 1

	ans = []

	for k, v in mpp.items():

		if v > (n // 3):
			ans.append(k)

	return ans


# better approach - using hashmap/dict but only a single iteration of arr
def majorityElementII_(arr):

	n = len(arr)
	mpp = {}
	ans = []

	for a in arr:
		if a in mpp:
			mpp[a] += 1
		else:
			mpp[a] = 1

		if mpp[a] == (n // 3) + 1:
			ans.append(a)
			
		if len(ans) == 2:
			break

	return ans


# optimal approach
# using the same intuition as we used for majority element(> n//2) problem [moore's voting algo]
# time complexity: O(n)
# extra space complexity: O(1)
def majorityElementII(arr):
    
    n = len(arr)
    
    count1 = 0
    count2 = 0

    el1 = float("-inf")
    el2 = float("-inf")

    for i in range(n):
        if count1 == 0 and arr[i] != el2:
            el1 = arr[i]
            count1 = 1
        elif count2 == 0 and arr[i] != el1:
            el2 = arr[i]
            count2 = 1
        elif arr[i] == el1:
            count1 += 1
        elif arr[i] == el2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    ans = []

    freq1 = 0
    for a in arr:
        if a == el1:
            freq1 += 1
    
    if freq1 > (n // 3):
        ans.append(el1)

    freq2 = 0
    for a in arr:
        if a == el2:
            freq2 += 1

    if freq2 > (n // 3):
        ans.append(el2)

    ans.sort()

    return ans