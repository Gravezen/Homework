
def fac(znach):
    a = znach
    for i in range(1, znach):
        a = a * i
    fac2(a)

def fac2(a):
    tmp = []
    while a > 0:
        b = a
        for o in range(1, a):
            b = b * o
        tmp.append(b)
        a -= 1
    print(tmp)

znach = int(input())
fac(znach)



