def remove_dup(x):
    if len(x) == 1:
        return x
    smalla = remove_dup(x[1:])
    if x[0] == x[1]:
        return smalla
    else:
        return x[0]+smalla


x = input()
print(remove_dup(x))
