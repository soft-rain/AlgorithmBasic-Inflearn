def fiboRec(n):
    if n <= 1:
        return n
    else:
        return fiboRec(n - 1) + fiboRec(n - 2)
