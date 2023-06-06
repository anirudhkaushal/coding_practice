from math import *
from collections import *
from sys import *
from os import *

# my approach:
# storing the freq of each element in a hash map/dict
# and then return the element whose freq is more than floor(n//2)
# time complexity: O(n)
# extra space taken to store freq in hash map/dict
def findMajorityElement(arr, n):
	
	freq = {}

	for a in arr:
		if a in freq:
			freq[a] += 1
		else:
			freq[a] = 1

	for k, v in freq.items():

		if v > (n // 2):
			return k

	return -1
		

# optimal approach:
# using moore's voting algorithm
# time complexity: O(2n)
# space complexity: O(1)
def findMajorityElement_optimal(arr, n):

	el = arr[0]
	count = 0

	for i in range(n):
		if count == 0:
			el = arr[i]
			count = 1
		elif arr[i] == el:
			count += 1
		else:
			count -= 1

	count2 = 0
	for a in arr:
		if a == el:
			count2 += 1

	if count2 > (n // 2):
		return el

	return -1