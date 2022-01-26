def power(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    ans = power(x*x, n//2)
    if n % 2 != 0:
        return x*ans
    else:
        return ans


x = int(input())
n = int(input())
a = power(x, abs(n))
if n >= 0:
    print(a)
else:
    print(1/a)
