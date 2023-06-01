def maxArea(arr):
    
    n = len(arr)
    i = 0
    j = n - 1

    prod = 1

    while i < j:

        prod = max((j - i) * min(arr[i], arr[j]), prod)

        if arr[i] > arr[j]:
            j -= 1
        elif arr[i] < arr[j]:
            i += 1
        else:
            if arr[i + 1] > arr[j - 1]:
                i += 1
            else:
                j -= 1

    return prod



