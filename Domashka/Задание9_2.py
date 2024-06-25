print("Введите количестно элементов 1-ого списка")
n = int(input())
print("Введите количестно элементов 2-ого списка")
N = int(input())
a1 = []
print("Введите последовательно элементы 1-ого списка")
for i in range(n):
    a = int(input())
    a1.append(a)
b1 = []
print("Введите последовательно элементы 2-ого списка")
for o in range(N):
    b = int(input())
    b1.append(b)

A1 = set(a1)
B1 = set(b1)
print("Количество элементов, одновременно содержащихся в двух списках:", len(A1.intersection(B1)))