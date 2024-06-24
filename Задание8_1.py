print("Веедите количество элеметов массива от 1 до 10000")
N = int(input())
if N <= 10000 and N >= 1:
    res = []
    print("Введите элемент по модулю не превышающий 1000000")
    while not len(res) == (N):
        for i in range(N):
            a = int(input())
            if abs(a) <= 10e5:
                res.append(a)
            else:
                print("Значение элемента превышено!")
    res.reverse()
    print(res)
else:
    print("Значение недопустимо!")