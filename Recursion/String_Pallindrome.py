def pallin(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return pallin(s[1:-1])
        else:
            return False


s = input()
if pallin(s):
    print("true")
else:
    print("false")
