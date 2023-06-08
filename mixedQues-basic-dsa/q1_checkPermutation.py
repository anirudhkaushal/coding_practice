from os import *
from sys import *
from collections import *
from math import *

# my approach - using 2 hashmap/dictionary; one for each str
def areAnagram_(str1, str2):
    # Write your code here.

    ans = 0
    
    mpp1 = {}
    mpp2 = {}

    for ch in str1:
        if ch in mpp1:
            mpp1[ch] += 1
        else:
            mpp1[ch] = 1

    for ch in str2:
        if ch in mpp2:
            mpp2[ch] += 1
        else:
            mpp2[ch] = 1

    for k, v in mpp1.items():
        if k in mpp2.keys() and mpp2[k] == v:
            ans = 1
        else:
            return 0

    return ans


# optimal approach - using a single hashmap
def areAnagram(str1, str2):

    mpp = {}

    if len(str1) != len(str2):
        return 0

    for ch in str1:
        if ch in mpp:
            mpp[ch] += 1
        else:
            mpp[ch] = 1

    for ch in str2:
        if ch in mpp:
            mpp[ch] -= 1

            if mpp[ch] < 0:
                return 0
        else:
            return 0

    return 1

