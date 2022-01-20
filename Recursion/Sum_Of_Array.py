def sum_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+sum_array(arr[1:])


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sum_array(arr))
