from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

# SOLUTION: the below function
# here, we first traverse the whole array to find largest element - O(n)
# then, we traverse the array again; in this traversal we don't look at the largest element anymore, thereby we find the next largest/second largest element - O(n)
# we also keep a variable named found which tells us whether there exists a second largest element 
# for e.g., in case of [9, 9, 9, 9] , there is no second largest element; hence, we return -1
# overall time complexity - O(n)
def findSecondLargest(sequenceOfNumbers):

    largest = float('-inf')
    secondlargest = float('-inf')
    found = 0

    for n in sequenceOfNumbers:
        if n > largest:
            largest = n

    for n in sequenceOfNumbers:
        if n == largest:
            pass
        elif n > secondlargest:
            found = 1
            secondlargest = n

    if found == 0:
        secondlargest = -1

    return secondlargest
        

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
