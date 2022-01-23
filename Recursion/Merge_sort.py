def merge(s1, s2, arr):
    i, j, k = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            arr[k] = s1[i]
            i += 1
            k += 1
        else:
            arr[k] = s2[j]
            j += 1
            k += 1
    while i < len(s1):
        arr[k] = s1[i]
        i += 1
        k += 1
    while j < len(s2):
        arr[k] = s2[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    s1 = arr[0:mid]
    s2 = arr[mid:]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, arr)


arr = [int(x) for x in input().split()]
merge_sort(arr)
print(arr)
