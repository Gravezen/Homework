# 🌲🟩🔥🌊⚡🚁💕⛪🏥 ⬛

from map import Map
import time # импортируем библиотеку тайм для установки частоты обновления
import os # импортируем библиотеку os для настройки отчистки консоли



TICK_SLEEP = 0.10 # задаём частоту кадров (обновления консоли)
TREE_UPDATE = 50 # задаём на каком кадре появится дерево (или нет, вдруг клетка уже занята)
FIRE_UPDATE = 100 # задаём обновление огня


tmp = Map(20, 10)
tmp.generate_forest(5, 10) # генерирует лес примерно 80%
tmp.generate_river(10) # генерируем реку длиной 5
tmp.print_map()

# покадровая отрисовка
tick = 1 # задаём тики, используя метод кадры

while True:
    os.system("CLS") # задаём отчистку экрана перед каждым тиком
    print("TICK", tick)
    tmp.print_map()
    tick += 1
    time.sleep(TICK_SLEEP) # указывает частоту обновления карты
    if (tick % TREE_UPDATE == 0): # если текущий тик делится без остатка на кадр появления дерева
        tmp.genetate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fire()