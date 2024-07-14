from utils import randcell

class Copter:

    def __init__(self, w, h): # функция задания вертолёта в случайном месте на карте
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.maxtank = 1
        self.score = 0

    def move(self, dx, dy): # функция перемещения вертолёта
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny
    
    def print_stats(self): # выводим меню
        print("🧺 ", self.tank, "/", self.maxtank, sep="", end=" | ")
        print("🥇", self.score) 
        