import collections

def create():
    name = input("Введите имя питомца: ")
    vid = input("Введите вид питомца: ")
    f = int(input("Введите возраст питомца: "))
    age1 = str(f) + age(f)
    vlad = input("Введите владельца питомца: ")
    name = {name: {"Вид питомца": vid, "Возраст питомца": age1, "Имя владельца": vlad}}
    if len(pets) == 0:
        pets[1] = name
    else:
        last = collections.deque(pets, maxlen=1)[0]
        pets[last + 1] = name

def get_pet(n):
    for id, name in pets.items():
        if n == id:
            return True
    else:
        print("Указанного питомца в словре нет!")
        return False

def pets_list():
    if len(pets) == 0:
        print("Список питомцев пуст!")
        return False
    else:
        for id, name in pets.items():
            print(id, name)

def read(n):
    if  get_pet(n) == False:
        return False
    for id, name in pets.items():
        if n == id and name != "Пусто":
            for key1, var in dict(name).items():
                var = dict(var)
                print(f'Это {var["Вид питомца"]} по кличке "{key1}". Возраст питомца: {var["Возраст питомца"]}. Имя владельца: {var["Имя владельца"]}.')
        elif n == id and name == "Пусто":
            print(name)
            print("Воспользуйтесь функцией 'update' для добавления информации в указанный раздел")

def update(n):
    if  get_pet(n) == False:
        return False
    name = input("Введите имя питомца: ")
    vid = input("Введите вид питомца: ")
    f = int(input("Введите возраст питомца: "))
    age1 = str(f) + age(f)
    vlad = input("Введите владельца питомца: ")
    name = {name: {"Вид питомца": vid, "Возраст питомца": age1, "Имя владельца": vlad}}
    pets[n] = name

def delete(n):
    if  get_pet(n) == False:
        return False
    name = "Пусто"
    pets[n] = name

def age(f):
    if f == 1 or f % 10 == 1 and f != 11:
        return(str(' год'))
    elif f == 2 or f == 3 or f == 4 or f % 10 == 2 and f != 12 or f % 10 == 3 and f != 13 or f % 10 == 4 and f != 14:
        return(str(' года'))
    else:
        return(str(' лет'))

command = input("Введите команду: ")
pets = {}
while command != "stop":
    if command == "create":
        create()
    elif command == "read":
        if pets_list() == False:
            print("Добавте питомца в словать!")
        else:
            n = int(input("Введите номер питомца в словаре: "))
            read(n)
    elif command == "update":
        if pets_list() == False:
            print("Добавте питомца в словать!")
        else:
            n = int(input("Введите номер питомца в словаре: "))
            update(n)
    elif command == "delete":
        if pets_list() == False:
            print("Добавте питомца в словать!")
        else:
            n = int(input("Введите номер питомца в словаре: "))
            delete(n)
    else:
        print("Введена ошибочная команда!")
        print("Доступные команды: create, read, update, delete, stop (остановка программы)")
    command = input("Введите команду: ")
else:
    exit()




