print("Введите максимальную массу (до 10000000), которую вмещает лодка")
m = int(input())
if m >=1 and m <= 10e6:
    print("Введите количество человек (до 100)")
    n = int(input())
    if n >=1 and n <= 100:
        print("Введите последовательно массу каждого человека, не превышающую вместимость лодки")
        res = []
        for i in range(n):
            a = int(input())
            if a >= 1 and a <= m:
                res.append(a)
            else:
                print("Превышена допустимая масса 1 человека")
                quit()
        res.sort(reverse=True)
        count = 0
        while len(res) >= 1:
            if (res[0] + res[-1]) <= m:
                res.pop(0)
                res.pop()
                count += 1
            else:
                res.pop(0)
                count +=1
        if len(res) == 0:
            print(count)
        else:
            count += 1
            print(count)
    else:
        print("Введено недопустимое количество человек!")
else:
    print("Введена недопустимая масса!")
