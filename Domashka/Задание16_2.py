class turtle(object):

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self, a):
        self.y += a * self.s

    def go_down(self, a):
        self.y -= a * self.s

    def go_left(self, a):
        self.x -= a * self.s

    def go_right(self, a):
        self.x += a * self.s

    def evolve(self):  # увеличивает s на 1
        self.s += 1
    
    def degrade(self):  # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.s == 1:
            print('Количество клеток перемещения черепашки не может быть меньше либо равно 0!!!')
        else:
            self.s -= 1

    def coordinates(self):
        print(f'Положение черепашки leonardo: X = {self.x}, Y = {self.y}')

    def raschet(self):
        x = self.x ** 2
        y = self.y ** 2
        sx = x - self.x
        sy = y - self.y
        count = 0
        if (sx <= sx * self.s) and (sy <= sy * self.s) and (sx < sy):
            object.go_up(sx)
            count += 1

        elif (sx <= sx * self.s) and (sy <= sy * self.s) and (sx > sy):
            object.go_rignt(sy)
            count += 1
        else:
            x

leonardo = turtle(15, 8, 1)
leonardo.coordinates()