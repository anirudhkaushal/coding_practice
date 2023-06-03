from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

# my approach : 
# 1. make a hash map(dict) which will have the count of 0s, 1s & 2s as values and O, 1 & 2 as key
# 2. sort the keys such that they're in sorted order 0 -> 1 -> 2
# 3. next we add the keys (0, 1, & 2) into new arr the no. of times they appear in original array
# time complexity: O(n) + O(k.log(k)) + O(n), where k = 3, since we have only 3 elements (0, 1, 2)
# space complexity: O(n) ; the new arr to store ans
# solution was accepted
def sort012(arr, n) :

    freq = {}

    for a in arr:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1

    ans = []

    freq_keys = list(freq.keys())
    freq_keys.sort()

    for k in freq_keys:

        val = freq[k]

        for i in range(val):
            ans.append(k)

    return ans


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    ans = sort012(arr, n)
    printAnswer(ans, n)
