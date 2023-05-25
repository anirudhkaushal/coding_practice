from os import *
from sys import *
from collections import *
from math import *



def firstNonRepeatingCharacter(str):

    # dict() is not ordered dictionary (ordered from Python version 3.7)
    # OrderedDict() is ordered dictionary
    freq = OrderedDict()

    for c in str:
        if c in freq:
            freq[c] += 1
            
        else:
            freq[c] = 1

    for x, y in freq.items():
        if y == 1:
            return x

    return str[0]
