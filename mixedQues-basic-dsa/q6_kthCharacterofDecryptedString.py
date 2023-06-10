from collections import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

# brute force approach - using hashmap as extra space
def kThCharaterOfDecryptedString_(s, k) :

	# Your code goes here
    cnt = 0
    i = 0
    mpp = OrderedDict()

    while i < len(s):
        if s[i].isalpha():
            cnt += 1
            i += 1

        else:
            substr = s[i - cnt: i]
            cnt = 0
            digitstr = ""

            while i < len(s) and s[i].isdigit():
                digitstr += s[i]
                i += 1

            if substr in mpp:
                mpp[substr] += int(digitstr)
            else:
                mpp[substr] = int(digitstr)

    exp_str = ""

    for key, vals in mpp.items():

        for i in range(vals):
            exp_str += key

    return exp_str[k-1]


# optimal approach - without using any extra space
def kThCharaterOfDecryptedString(s, k):

    cnt = 0
    i = 0

    while i < len(s):
        if s[i].isalpha():
            cnt += 1
            i += 1

        else:
            substr = s[i - cnt: i]
            cnt = 0
            digitstr = ""

            while i < len(s) and s[i].isdigit():
                digitstr += s[i]
                i += 1

            n = len(substr)
            freq = n * int(digitstr)

            if k <= freq:
                k = k % n
                return substr[k - 1]
            else:
                k = k - freq

    return -1



























#taking inpit using fast I/O
def takeInput() :
	
    str1 = input().strip()
    k = int(input().strip())

    return str1, k

#main
str1, k = takeInput()
print(kThCharaterOfDecryptedString(str1, k))
