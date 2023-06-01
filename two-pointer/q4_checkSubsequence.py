from os import *
from sys import *
from collections import *
from math import *

def isSubSequence(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    i = 0
    
    for j in range(n2):
        if str1[i] == str2[j]:
            i += 1

    if i == n1:
        return True

    return False

