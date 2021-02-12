def ladd(u, v):
    n = len(u) if len(u) > len(v) else len(v)
    result = []
    carry = 0
    for k in range(n):  ##0~n-1까지
        i = u[k] if (k < len(u)) else 0
        j = v[k] if (k < len(v)) else 0
        value = i + j + carry
        carry = value // 10
        result.append(value % 10)
    if (carry > 0):
        result.append(carry)
    return result

#파이썬은 디폴트가 long임!
