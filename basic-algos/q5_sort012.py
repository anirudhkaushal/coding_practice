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
# space complexity: O(n) ; the new arr to store ans + for storing hash map/dict
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

# better approach: instead of hashmap we maintain 3 variables for count since we have only 0s, 1s, and 2s
# also in this approach, we do not create a new array; we simply overwrite the original array
# time complexity: O(n) + O(n)
# space complexity: O(1)
def sort012_better(arr, n) :

    count0 = 0
    count1 = 0
    count2 = 0

    for a in arr:
        if a == 0:
            count0 += 1
        elif a == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(count0):
        arr[i] = 0
    
    for i in range(count0, count0 + count1):
        arr[i] = 1
    
    for i in range(count0 + count1, n):
        arr[i] = 2


# optimal approach: using dutch national flag algo
# time complexity: O(n)
# space complexity: O(1)
def sort012_optimal(arr, n):

    low = 0
    mid = 0
    high = n - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1




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
