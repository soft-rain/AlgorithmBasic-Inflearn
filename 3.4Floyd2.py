def floyd2(W):
    n = len(W)
    D = W
    P = [[-1] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (D[i][j] > D[i][k] + D[k][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
    return D, P
