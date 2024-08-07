class Car(object): # object базовый класс
    brand = 'Mazda'
    color = 'black'
    max_speed = 100

    def __init__(self, b, ms): # конструктор
        self.brand = b # изменяемые атрибуты, переданы в скобках после self
        self.max_speed = ms 

    def apgrade(self): # метод
        self.max_speed += 25 # после вызова функции скороть объекта будет увеличиваться на 25
    
nissan = Car('Nissan', 190) # создаём класс Ниссан, скорость 190
print(nissan.brand, nissan.max_speed) # выводим атрибуты объекта класса

# НАССЛЕДОВАНИЕ
# добавляет новый класс, наследующий все свойства предыдущего класс + добавляет что-то новое

class Truck(Car): # в скобках прописывается класс, от которого всё наследуется
    max_weight = 10

    def __init__(self, b, ms, mw):
        super().__init__(b, ms) # включаем свойства из насследованного класса!
        self.max_weight = mw # добавляем в наследованный класс дополнителное свойство в конструктор
        
    def add(self):
        self.max_weight += 10 # также можно добавлять дополнительные методы
# однако добавленные свойства и методы не будут работать в родительском классе!

# ГЛАВНОЕ при создании объекта не забывать, что в начальном классе
# при создании объекта вводились обязательные атрибуты!!!
gazel = Truck('Gazel', 60)
print(gazel.max_weight) # выведем новый атрибут из объекта Gazel

# ПРИВАТНОСТЬ ПОЛЕЙ (свойств и методов)
class Car(object): # object базовый класс
    brand = 'Mazda'
    color = 'black'
    max_speed = 100
    __password = 1234 # два нижних подчёркивания перед свойством или функцией 
    # делают их приватными, т.е. неизменяемыми, ОЧ ПОЛЕЗНО
    # обратиться к нему обычным методом не получится
    # для вывода используется функция
    def get_password(self):
        return self.__password
    
    def __update_password(self):
        self.__password = 234 

    def apgrade(self): 
        self.max_speed += 25 
        self.__update_password() # при выполнении метода apgrade будет выполняться метод зменения пароля
    # вне класса обратиться к методу __upgrade_password не получится!!)

nissan._Car__password = 123 #ОДНАКО так всёравно можно изменить значение
# приватного свойства или функции, но делать эта сложна да и нахер надо



