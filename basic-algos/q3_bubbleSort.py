from os import *
from sys import *
from collections import *
from math import *

def bubbleSort(arr,n):
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
            
