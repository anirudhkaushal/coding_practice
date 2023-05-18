from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    left = 0
    right = 0

    for i in range(len(pattern)):

        if pattern[i] == ')':
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            left += 1

    return left+right      
