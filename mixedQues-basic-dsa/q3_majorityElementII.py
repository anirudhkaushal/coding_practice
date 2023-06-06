from math import *
from collections import *
from sys import *
from os import *

# my approach - using hashmap/dictionary
def majorityElementII(arr):
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