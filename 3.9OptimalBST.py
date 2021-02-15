def optsearchtree(p):
    n = len(p) - 1
    A = [[-1] * (n + 1) for _ in range(n + 2)]
    R = [[-1] * (n + 1) for _ in range(n + 2)]
    for i in range(1, n + 1):
        A[i][i - 1] = 0
        A[i][i] = p[i]
        R[i][i - 1] = 0
        R[i][i] = i
    A[n + 1][n] = 0
    R[n + 1][n] = 0
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            A[i][j], R[i][j] = minimum(A, p, i, j)
    return A, R


def minimum(A, p, i, j):
    minValue = INF
    minK = 0
    for k in range(i, j + 1):
        value = A[i][k - 1] + A[k + 1][j]
        for m in range(i, j + 1):
            value += p[m]
            if minValue > value:
                minValue = value
                minK = k
    return minValue, minK


INF = 999
keys = [0, 10, 20, 30, 40, 50]
p = [0, 35, 12, 22, 8, 15]
A, R = optsearchtree(p)
print('A = ')
for i in range(1, len(A)):
    print(A[i])
print('R = ')
for i in range(1, len(R)):
    print(R[i])
