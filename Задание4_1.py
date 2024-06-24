print("введите последовательно стороны треугольника")
a = float(input())
b = float(input())
c = float(input())

P = a + b + c
p = (1 / 2) * P
S = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

print("Периметр треугольника равен", float(P), ", его площадь равна", float(S))