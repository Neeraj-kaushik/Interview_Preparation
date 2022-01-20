def lastNum(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    a = arr[1:]
    smalla = lastNum(a, x)
    if smalla != -1:
        return smalla+1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())
print(lastNum(arr, x))
