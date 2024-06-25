print("Введите значения A и B, где A меньше, либо равно B")
A = int(input())
B = int(input())
if A > B:
    print("A не может быть больше B!")
else:   
    for i in range(A, B + 1):
        if i % 2 == 0:
            print(i)