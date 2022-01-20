def firstIndex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    a = arr[1:]
    smalla = firstIndex(a, x)
    if smalla == -1:
        return -1
    else:
        return smalla+1


n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())
print(firstIndex(arr, x))
