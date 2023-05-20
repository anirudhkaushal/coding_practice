from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)


def nextLargestPalindrome(s, length):
    
    s_list = []

    for val in s:
        s_list.append(int(val))

    # incrementing the number by one such that it is not a pallindrome anymore
    len0 = length - 1
    k = 0
    n = 0
    while(len0 >= 0):
        n += s_list[k] * (10**len0)
        len0 -= 1
        k += 1

    n += 1

    s_list.clear()

    temp_n = n
    while(temp_n > 0):
        rem = temp_n % 10
        temp_n = temp_n // 10
        s_list.append(rem)

    s_list.reverse()

    ans = "hello"

    # code for odd length string/number
    if length % 2 != 0:

        mid = length // 2

        leftHalf = s_list[:mid]
        rightHalf = s_list[mid+1:]

        # reversing the left half
        leftHalf.reverse()

        # calculating the value of left half
        len1 = len(leftHalf) - 1
        i = 0
        ln = 0
        while(len1 >= 0):
            ln += leftHalf[i] * (10**len1)
            len1 -= 1
            i += 1

        # calculating value of right half
        len2 = len(rightHalf) - 1
        j = 0
        rn = 0
        while(len2 >= 0):
            rn += rightHalf[j] * (10**len2)
            len2 -= 1
            j += 1

        if ln > rn:
            ans = str(s_list[:mid+1] + leftHalf)
        else:
            s_list[mid] += 1
            ans = str(s_list[:mid+1] + leftHalf)

    return ans
            




































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
