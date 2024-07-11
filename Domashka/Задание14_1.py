my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
n = len(my_list)

def tmp(n):
    n = n - 1
    if len(my_list) == n:
        return n
    elif len(my_list) == 0:
        return
    print(my_list[0])
    my_list.pop(0)
    tmp(n)


tmp(n)