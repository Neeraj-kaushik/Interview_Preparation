def t_o_h(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    t_o_h(n-1, a, c, b)
    print(a, c)
    t_o_h(n-1, b, a, c)


n = int(input())
if n == 0:
    print("")
else:
    t_o_h(n, 'a', 'b', 'c')
