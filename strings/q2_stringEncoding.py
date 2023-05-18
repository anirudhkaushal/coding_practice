from os import *
from sys import *
from collections import *
from math import *

def encode(message):
    
    output = ""

    count = 1
    chr = message[0]
    for i in range(1, len(message)):

        if message[i] == chr:
            count += 1
        else:
            output = output + chr + str(count)
            chr = message[i]
            count = 1 

    output = output + chr + str(count)

    return output     