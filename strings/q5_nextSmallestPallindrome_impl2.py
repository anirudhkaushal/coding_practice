from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def compare(x, y):
    for i, j in zip(x, y):
        if int(i) > int(j):
            return 1
        elif int(i) < int(j):
            return -1
        else:
            continue
    return 0
        

def nextLargestPalindrome(s, length):
    
    # adding 1 to the number such that it is no longer a pallindrome
    
    if length > 1:
        s = str(int(s) + 1)

    if len(s) % 2 != 0: #handling odd length case
        n = len(s)
        
        left = s[:n//2]
        mid = s[n//2]
        right = s[n//2+1:]

        if compare(left[::-1], right) == 1:
            return left + mid + left[::-1]
        else:
            left = left + mid
            left = str(int(left) + 1)
            return left + left[::-1][1:]
    else: # handling even length cases
        n = len(s)
        
        left = s[:n//2]
        right = s[n//2:]
        
        if compare(left[::-1], right) == 1:
            return left + left[::-1]
        else:
            left = str(int(left) + 1)
            return left + left[::-1]
    
        

# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    return N, S


tc = int(input())
while tc > 0:
    N, S = takeInput()
    S = nextLargestPalindrome(S, N)
    stdout.write(S + "\n")
    tc -= 1
