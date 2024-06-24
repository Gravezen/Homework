print("Введите через пробел элементы")
res = list(map(int, input().split()))
mn = set(res)
print("Количество разных элементов:", len(mn))