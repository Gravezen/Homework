s = input("Введите строку:")
a = 0
b = 0
c = set("aeiou")
for letter in s:
    if letter in c:
        a += 1
    else:
        b += 1
print("Количество гласных равно:", a)
print("Количество согласных равно:", b)
d = s.count("a")
if d > 0:
    print("Количество гласный a =", d)
else:
    print("Гласный a в строке нет!")
e = s.count("e")
if e > 0:
    print("Количество гласный e =", e)
else:
    print("Гласный e в строке нет!")
f = s.count("i")
if f > 0:
    print("Количество гласный i =", f)
else:
    print("Гласный i в строке нет!")
g = s.count("o")
if g > 0:
    print("Количество гласный o =", g)
else:
    print("Гласный o в строке нет!")
h = s.count("u")
if h > 0:
    print("Количество гласный u =", h)
else:
    print("Гласный u в строке нет!")
