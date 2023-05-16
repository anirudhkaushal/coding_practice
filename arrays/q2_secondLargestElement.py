from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

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
