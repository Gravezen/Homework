# 🌲🟩🔥🌊⚡🚁💕⛪🏥 ⬛ 🧺 🥇

from map import Map
import time # импортируем библиотеку тайм для установки частоты обновления
import os # импортируем библиотеку os для настройки отчистки консоли
from copter import Copter as Coptero
from pynput import keyboard # импортируем библиотку считывания клавиатуры


TICK_SLEEP = 0.1 # задаём частоту кадров (обновления консоли)
TREE_UPDATE = 50 # задаём на каком кадре появится дерево (или нет, вдруг клетка уже занята)
FIRE_UPDATE = 100 # задаём обновление огня
MAP_W, MAP_H = 20, 10

copter = Coptero(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a' : (0, -1)} # словарь перемещений

def on_press(key):
    c = key.char.lower() # ключ равен символом в нижнем регистре, перевод сразу в него
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        copter.move(dx, dy)
listener = keyboard.Listener(
    on_press=on_press,
    on_release=None)
listener.start()

tmp = Map(MAP_W, MAP_H)

# покадровая отрисовка
tick = 1 # задаём тики, используя метод кадры

while True:
    os.system("CLS") # задаём отчистку экрана перед каждым тиком
    print("TICK", tick)
    tmp.process_copter(copter)
    copter.print_stats()
    tmp.print_map(copter)
    tick += 1
    time.sleep(TICK_SLEEP) # указывает частоту обновления карты
    if (tick % TREE_UPDATE == 0): # если текущий тик делится без остатка на кадр появления дерева
        tmp.genetate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fire()