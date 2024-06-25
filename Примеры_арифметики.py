# a = int(input()) # int обращает строку в число, если возможно
# b = int(input())
# print(a * b) # арифимитическая операция

# a = input().split() # разделяет строку (если вводить с пробелом)

# a, b = input().split() # вводит 2 переменные через пробел

# a, b = map(int, input().split()) # map выполняет функцию int каждому значению из input().split()
# print(a * b)

# a, b, c = input().split() # вариант без map
# a = int(a)

# a = int(input())
# b = int(input()) # или c = a + b
# print(a + b)     #     print(c)

a, b = map(int, input().split())
c = (a + b) * 4 # или сосздать d = a + b, потом уже c = d * 4
print(c)

a = float(input()) # float делает число вещественным 5.0 пишет
print(a)
