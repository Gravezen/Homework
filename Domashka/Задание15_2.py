class Transport(object):

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobas(Transport):
    capacity = 20


Renaul = Autobas('Renaul Logan', 180, 12)
print(Renaul.seating_capacity(50))