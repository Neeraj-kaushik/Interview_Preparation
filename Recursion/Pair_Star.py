def pair_star(s, s1, i):
    s1 = s1+s[i]
    if i == len(s)-1:
        print(s1)
        return
    if s[i] == s[i+1]:
        s1 = s1+'*'
    pair_star(s, s1, i+1)


s = input()
s1 = ""
i = 0
pair_star(s, s1, i)
