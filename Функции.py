def chet(a): #задаем функцию, в круглых скобках через
# запятую задаются параметры, которые передаются в фукнцию
    if a % 2 == 0: # если "a" чётное
        return True # возвращаем значение функции
    # после return больше ничего выполняться не будет внутри функции
    else: # можно убрать else, так как если число будет
        # не чётное, выполнится программа далее после return True
        return False
    
print(chet(4))


def tmp(name):
    print(f'Hello, {name}')
    # вызвав функцию и вписав имя, функция пишет это имя в заданной строке
tmp('Mark') # т.к. в функции уже есть функция print, просто вызываем функцию

# сложнее!!!

def vis(year): # (если год кратен 4, и не кратен 100) или (кратен 400)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True # выводим "Правда"
    return False # выводим "Ложь"

year = int(input()) # вводим год
print(vis(year)) # выводим вызов функции от года!

# ЕЩЁ!!
def nechet(n):
    return (n % 2 != 0) # сокращенная функция
    # если число нечетное, выводим true, иначе false

def res(l): # функция вызова списка
    for i in l: # проходимся по значениям списка
        if nechet(i): # если значение списка возвращает значение функии
            print(i) # nechet = true, выводим это значение

list = [1, 3, 4, 9, 2] # заданный список
res(list) # запускаем функцию res от списка
# выводом будут все нечётные значения в списке!!!

# прикладная задача!?
# CHAT BOT POZDRAVITEL

def new_year(): # здесь не надо передавать никакое значение
    print('Heppy New Year!') # обращение к функции запустис поздравление!

def birthday(uname): # Тут нужно указать имя, чтоб к нему обращались!
    # name = input() можем сюда подставить, чтоб ниже не вставлять! из скобок в функции надо убрать name
    print(f'Happy Birthday, {uname}!')

def mart8(): # аналогично первой функции!
    print(f'Happy 8th of March!')

n = int(input()) # вводим количество поздравлений!
for i in range(n): # для каждого из количества поздравлений:
    cm = input() # вводим команду
    if cm == 'new Year': # если команда такая то:
        new_year() # вызываем функцию
    elif cm == 'birthday': # аналогично!
        uname = input() # но сначало вводим имя!
        birthday(uname)
    elif cm == "8 march": # аналогично!
        mart8()
    else: # если написали дичь, то напишут что ошибочная команда!
        print("Wrong command!")
    
