def check_num(arr, x):
    l = len(arr)
    if l == 0:
        return False
    if arr[0] == x:
        return True
    a = arr[1:]
    smalla = check_num(a, x)
    return smalla


n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())
if check_num(arr, x):
    print('true')
else:
    print('false')
