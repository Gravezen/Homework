print ("Введите строку, длиной не превышающей 1000 знаков")
a = str(input())
if len(a) > 1000:
    print("Первышена допустимая длина строки!")
else:
    print(" ".join(a.split()))

