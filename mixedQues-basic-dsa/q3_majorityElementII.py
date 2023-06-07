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
def majorityElementII(arr):

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