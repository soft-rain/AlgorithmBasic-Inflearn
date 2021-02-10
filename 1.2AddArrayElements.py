def sum(n, S):
    result = 0
    for i in range(0, n + 1):
        result += S[i]
    return result


# example
S = [-1, 10, 7, 11, 5, 13, 8]
sum = sum(len(S) - 1, S)
print(sum)

