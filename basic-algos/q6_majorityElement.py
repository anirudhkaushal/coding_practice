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
		