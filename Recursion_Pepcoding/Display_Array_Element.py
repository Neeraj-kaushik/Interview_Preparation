def print_arr(li):
    if len(li) == 1:
        print(li[0])
        return
    print(li[0], end=" ")
    print_arr(li[1:])


n = int(input())
li = [int(x) for x in input().split()]
print_arr(li)
