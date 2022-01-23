def pivot(a, si, ei):
    x = a[si]
    count = 0
    for i in range(si, ei+1):
        if a[i] < x:
            count += 1
    a[si+count], a[si] = a[si], a[si+count]
    index = si+count
    i = si
    j = ei
    while i < j:
        if a[i] < x:
            i += 1
        elif a[j] >= x:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return index


def quick_Sort(a, si, ei):
    if si >= ei:
        return
    pivot_index = pivot(a, si, ei)
    quick_Sort(a, si, pivot_index-1)
    quick_Sort(a, pivot_index+1, ei)


a = [int(x) for x in input().split()]
quick_Sort(a, 0, len(a)-1)
print(a)
