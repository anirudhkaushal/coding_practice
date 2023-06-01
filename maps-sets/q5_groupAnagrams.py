from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getGroupedAnagrams(inputStr):
    
    res = {} # mapping charCount to list of anagrams

    for s in inputStr:
        count = [0]*26 # a ... z

        for ch in s:
            count[ord(ch) - ord("a")] += 1

        if tuple(count) in res: 
            res[tuple(count)].append(s) #in python, list are mutable and hence cannot be used as a key in dict; hence we convert it to a tuple first
        else:
            s_list = []
            s_list.append(s)
            res[tuple(count)] = s_list

    ans_list = []
    for v in res.values():
        ans_list.append(v)

    return ans_list


        


    

def takeInput():

    n = stdin.readline().strip()
    inputStr = list(stdin.readline().strip().split(" "))

    return inputStr, n


def printAnswer(groupedAnagram):
    for group in groupedAnagram:
        group.sort()

    groupedAnagram.sort()

    print('\n'.join(map(' '.join, groupedAnagram)))


T = int(stdin.readline().strip())
for i in range(T):
    inputStr, n = takeInput()
    groupedAnagram = getGroupedAnagrams(inputStr)
    printAnswer(groupedAnagram)
