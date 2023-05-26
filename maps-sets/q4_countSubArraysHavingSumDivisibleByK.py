from os import *
from sys import *
from collections import *
from math import *

# my approach - brute force with O(n^2) time complexity (did not get accepted - time limit exceeded)
def subArrayCount(arr, k):

    # s = set()
    n = len(arr)
    count = 0

    for i in range(n):
        sum = arr[i]

        if sum % k == 0:
            count += 1

        for j in range(i+1, n):
            sum += arr[j]

            if sum % k == 0:
                count += 1

    return count


# optimal approach: O(n) time complexity using hash map
from os import *
from sys import *
from collections import *
from math import *

def subArrayCount_optimal(arr, k):

    n = len(arr)
    hmap = dict()

    sum = 0
    hmap[0] = 0

    count = 0
    for i in range(n):
        sum += arr[i]

        # here, we need to handle the case when sum is negative; 
        # when rem is -ve, we simply add k to the sum (for c++, java)
        # however, python handles modulo of -ve numbers; so its not necessary but i have still added that logic
        rem = sum % k

        if rem in hmap:
            hmap[rem] += 1
            count += hmap[rem]
        else:
            hmap[rem] = 0

    return count
