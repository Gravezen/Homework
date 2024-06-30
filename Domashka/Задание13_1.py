import random

def pt(name):
    for y in name:
        print(y)

def matrix1(a, b):
    matr = [[0 for i in range(a)] for i in range(b)]
    for i in range(b):
        for j in range(a):
            c = int(random.randint(-100, 100))
            matr[i][j] = c
    return matr    

def matrix2(a, b):
    matr = [[0 for i in range(a)] for i in range(b)]
    for i in range(b):
        for j in range(a):
            c = int(random.randint(-100, 100))
            matr[i][j] = c    
    return matr    
   

def sum_matrix(a, b):
    matr1 = matrix1(a, b)
    matr2 = matrix2(a, b)
    sumatr = [[0 for i in range(a)] for i in range(b)]
    for i in range(b):
        for j in range(a):
            d = matr1[i][j] + matr2[i][j]
            sumatr[i][j] = d
    print(f"Матрица №1 с числом строк {b} и числом столбцов {a}")
    pt(matr1)
    print(f"Матрица №2 с числом строк {b} и числом столбцов {a}")
    pt(matr2)
    print(f"Сумма матриц №1 и №2 c числом строк {b} и числом столбцов {a}")
    pt(sumatr)

a = int(random.randint(1, 20)) # значения можно увеличить, сделано для примера!
b = int(random.randint(1, 20)) # значения можно увеличить, сделано для примера!
sum_matrix(a, b)
