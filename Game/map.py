from utils import randbool # импортируем функцию из файла
from utils import randcell # импортируем ещё функцию из файла
from utils import randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд шоп
# 5 - огонь

CELL_TYPES = '🟩🌲🌊🏥⛪🔥'
TREE_BONUS = 100
UPGRADE_PRICE = 500

class Map:
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(5, 10) # генерирует лес примерно 50%
        self.generate_river(10) # генерируем реку длиной 10
        self.generate_river(10) # генерируем реку длиной 10
        self.generate_upgrade_shop() # генерируем магазин
        
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def print_map(self, copter):
        print('⬛' * (self.w + 2)) # вводим рамку
        for ri in range(self.h): # вводим поля
            print('⬛', end="") # вводим рамку
            for ci in range(self.w): # 2 цикла, так как список в списке
                cell = self.cells[ri][ci]
                if (copter.x == ri and copter.y == ci): # в конкретный момент времени, вертолёт будет замещать клетку
                    print('🚁',end="")
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")           
            print('⬛') # вводим рамку
        print('⬛' * (self.w + 2))

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

    def genetate_tree(self): # функция генерации деревьев
        c = randcell(self.w, self.h) # выбираем функцию случайной клеточки
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0): # если клетка проходит проверку и на её месте 0 (поле)
            self.cells[cx][cy] = 1 # сажаем туда дерево :)

    def generate_forest(self, r, mxr): # r - диапазон рандома, mxr - отсечка(если показатель рандома выше определенного значения, отсекаем)
        for ri in range(self.h): # проходимся по полю (map)
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h) # выбираем функцию случайной клеточки
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4 # ставим туда магазин :)

    def add_fire(self): # добавляем огонь!
        c = randcell(self.w, self.h) # выбираем функцию случайной клеточки
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 1): # если клетка проходит проверку и на её месте 1 (дерево)
            self.cells[cx][cy] = 5 # помещаем туда огонь! ааа

    def update_fire(self): # обновляем огонь!
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.add_fire()

    def process_copter(self, copter):
        c = self.cells[copter.x][copter.y] 
        if (c == 2):
            copter.tank = copter.maxtank
        if (c == 5 and copter.tank > 0):
            copter.tank -= 1
            copter.score += TREE_BONUS
            self.cells[copter.x][copter.y] = 1
        if (c == 4 and copter.score >= UPGRADE_PRICE):
            copter.maxtank += 1
            copter.score -= UPGRADE_PRICE
        
            
