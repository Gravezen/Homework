print("Веедите количество элеметов массива от 1 до 100000")
N = int(input())
if N <= 100000 and N >= 1:
    print("Введите через пробел элементы, значения от 1 до 10000000000")
    res = list(map(int, input().split()))
    if not len(res) == N:
        print("Заданное количество элементов массива не выполнено!")
    else:
        new = []
        for o in res:
            if o < 1 or o > 10e9:
                print("Введено недопустимое значение списка")
                quit()
            else:
                new.append(o)
        new.reverse()
        while not len(new) == 1:
            new.pop()
        for o in res:
            new.append(o)
        new.pop()
        print(new)          
else:
    print("Значение недопустимо!")