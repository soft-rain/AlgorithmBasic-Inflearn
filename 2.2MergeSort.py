def mergeSort(S):
    n = len(S)
    if (n <= 1):
        return S
    else:
        mid = n // 2
        U = mergeSort(S[0:mid])  # Slicing(S[mid]~S[n-1]
        V = mergeSort(S[mid:n])
        print("U = ", U, end=" ")
        print("V = ", V)
        return merge(U, V)


def merge(U, V):
    S = []
    i = j = 0
    while (i < len(U) and j < len(V)):
        if (U[i] < V[j]):
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j += 1
        if (i < len(U)):
            S += U[i:len(U)]
        else:
            S += V[j:len(V)]
        return S


S = [27, 10, 12, 20, 25, 13, 15, 22]
print(S)
X = mergeSort(S)
print(X)
