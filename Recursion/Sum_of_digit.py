def sum_digit(a):
    if a == 0:
        return 0
    return (a % 10+sum_digit(a//10))


n = int(input())
x = sum_digit(n)
print(x)
