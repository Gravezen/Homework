class Transport(object):

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Autobus = Transport('Renaul Logan', 180, 12)

print(f'Наименование автомобиля: {Autobus.name} Cкорость: {Autobus.max_speed} Пробег: {Autobus.mileage}')