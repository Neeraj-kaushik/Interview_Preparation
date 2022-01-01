def multi(m, n):
    if n == 1:
        return m
    return m+multi(m, n-1)


m = int(input())
n = int(input())
print(multi(m, n))
