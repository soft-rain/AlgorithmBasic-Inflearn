def quickSort(S, low, high):
    if (high > low):
        pivotpoint = partition(S, low, high)
        quickSort(S, low, pivotpoint - 1)
        print(S)
        print(pivotpoint)
        quickSort(S, pivotpoint + 1, high)
        print(S)
        print(pivotpoint)

def partition(S,low,high):
    pivotitem=S[low]
    j=low
    for i in range(low+1, high+1):
        if(S[i]<pivotitem):
            j+=1
            S[i],S[j]=S[j],S[i]
    pivotpoint=j
    S[low],S[pivotpoint] = S[pivotpoint],S[low]
    return pivotpoint

print("quickSort")
S=[15,22,13,27,12,10,20,25]
print("Before : ", S)
quickSort(S, 0, len(S) - 1)
print("After : ", S)

print("partition")
S=[15,22,13,27,12,10,20,25]
print("Before : ", S)
partition(S, 0, len(S) - 1)
print("After : ", S)