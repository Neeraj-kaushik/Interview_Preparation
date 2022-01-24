def st_in(s):
    if len(s) == 1:
        return ord(s[0])-ord('0')
    a = st_in(s[1:])
    a1 = ord(s[0])-ord('0')
    a1 = a1*(10**(len(s)-1))+a
    return int(a1)


s = input()
print(st_in(s))
