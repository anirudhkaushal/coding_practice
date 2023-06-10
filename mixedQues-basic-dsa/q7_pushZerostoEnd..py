# using the partition approach

def pushZerosAtEnd(arr):
    # write your code here

    n = len(arr)
    i = -1
    pivot = 0

    for j in range(n):

        if arr[j] != pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr