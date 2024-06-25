a = int(input())

if a == 0:
    print("нулевое число!")
elif a < 0 and a / 2 == int(a / 2):
    print("отрицательное четное число")
elif a < 0 and a / 2 == float(a / 2):
    print("отрицательное нечетное число")
elif a > 0 and a / 2 == int(a / 2):
    print("положительное четное число")
else:
    print("положительное нечетное число")
