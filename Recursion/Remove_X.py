def remove(s1):
    if len(s1) == 0:
        return s1
    smalla = remove(s1[1:])
    if s1[0] == 'x':
        return smalla
    else:
        return s1[0]+smalla


s1 = input()
print(remove(s1))
