print("Введите пятизначное число (первая и вторая цифра числа не должны быть одинаковыми)")
a = input()
b = (int(a[3]) ** int(a[4])) * int(a[2]) / (int(a[0]) - int(a[1]))
print(float(b))
