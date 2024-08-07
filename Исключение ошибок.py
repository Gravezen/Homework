# ОБРАБОТКА ОШИБОК
t = [1, 2, 5]

try: # пробуем код
    print(45//0) # на ноль делить не получится!
    print(t[10]) # если не указать ниже ошибку, то программа остановится!
except ZeroDivisionError: # пишем какую ошибку исключаем
    print('Не надо так, делить на 0, нельзя!') # пишем, что при этом будет просиходить
except IndexError:
    print('Такого индекса нет, попробуйте другой') # добавляем ещё условие исключения!
except Exception: # если не знаем, что может случится, пишем так, выведется ответ на любую ошибку!
    print('Возникла какая-то ошибка!')
# программа продолжает выполняться дальше!!
else: # выполняется, когда не произошло не одной ошибки!
    print('Всё нормально!')
finally:  # тут прописывается действие, которое произойдёт в любом случае, была ли ошибка или нет
    print('конец')
print('Тест')

# Обработка ошибок работает только на первую ошибку, если ничего не писать

# О-НОТАЦИЯ - оценивает сложность программы!
n = int(input())
a = 1
for i in range(n):
    for j in range(n):
        a += 1

# O(n ^ 2) - скорость обработки этой программы выше
#  скорость питона 10 ** 6 операций, внимательно!