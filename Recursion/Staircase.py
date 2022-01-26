def stair(n):
    if n < 3:
        return n
    if n == 3:
        return 4
    return stair(n-1)+stair(n-2)+stair(n-3)


n = int(input())
count = stair(n)
print(count)
