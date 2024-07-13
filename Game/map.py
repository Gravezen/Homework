from utils import randbool # импортируем функцию из файла
from utils import randcell # импортируем ещё функцию из файла
from utils import randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд шоп

class Map:
    
    def generate_river(self, l): # функция создания реки, где l - длина реки
        rc = randcell(self.w, self.h) # задаётся список, выраженный координатами устья реки
        rx, ry = rc[0], rc[1] # переприсваем значения rc, чтоб было проще
        if (self.check_bounds(rx, ry)):
            self.cells[rx][ry] = 2 # в указанном списке берем 2 значения, там ставим реку
            while l > 0:
                rc2 = randcell2(rx, ry)
                rx2, ry2 = rc2[0], rc2[1]
                if (self.check_bounds(rx2, ry2)): # выполняем проверку новой клетки, чтоб не вышла за поле!
                    self.cells[rx2][ry2] = 2 # если всё ок, в получившуюся клетку ставим воду
                    rx, ry = rx2, ry2 # заменяем начальные координаты на координаты следующей клетки
                    l -= 1 # уменьшаем длину реки

    def generate_forest(self, r, mxr): # r - диапазон рандома, mxr - отсечка(если показатель рандома выше определенного значения, отсекаем)
        for ri in range(self.h): # проходимся по полю (map)
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def print_map(self):
        print('⬛' * (self.w + 2)) # вводим рамку
        for row in self.cells: # вводим поля
            print('⬛', end="") # вводим рамку
            for cell in row: # 2 цикла, так как список в списке
                if cell == 0:
                    print('🟩', end="") # в конце ставим ничего, чтоб не перекидывало на другую строку
                elif cell == 1:
                    print('🌲', end="")
                elif cell == 2:
                    print('🌊', end="")
                elif cell == 3:
                    print('🏥', end="")
                elif cell == 4:
                    print('⛪', end="")
            print('⬛') # вводим рамку
        print('⬛' * (self.w + 2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


tmp = Map(10, 20)
tmp.generate_forest(7, 10) # генерирует лес примерно 80%
tmp.generate_river(5) # генерируем реку длиной 5
tmp.print_map()