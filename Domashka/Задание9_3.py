print("Введите через пробел числа")
A = list(map(int, input().split()))
B = set()
for i in A:
    if i in B:
        print("YES")
    else:
        print("NO")
        B.add(i)