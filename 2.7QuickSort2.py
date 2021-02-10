def quickSort2(S, low, high):
    if (high > low):
        pivotpoint = partition2(S, low, high)
        quickSort2(S, low, pivotpoint - 1)
        print(S)
        print(pivotpoint)
        quickSort2(S, pivotpoint + 1, high)
        print(S)
        print(pivotpoint)


def partition2(S, low, high):
    pivotitem = S[low]
    ##QuickSort1과 차이점
    i = low + 1
    j = high
    while (i <= j):
        while (S[i] < pivotitem):
            i += 1
        while (S[j] > pivotitem):
            j -= 1
        if (i < j):
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint


print("quickSort")
S = [15, 22, 13, 27, 12, 10, 20, 25]
print("Before : ", S)
quickSort2(S, 0, len(S) - 1)
print("After : ", S)

print("partition")
S = [15, 22, 13, 27, 12, 10, 20, 25]
print("Before : ", S)
partition2(S, 0, len(S) - 1)
print("After : ", S)
