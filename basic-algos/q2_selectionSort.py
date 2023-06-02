from os import *
from sys import *
from collections import *
from math import *

def selectionSort(arr,n):
    
    for i in range(n):
        min = float("inf")

        for j in range(i, n):
            if arr[j] < min:
                min = arr[j]
                min_idx = j

        # if arr[i] == arr[min_idx]:

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

        
        

