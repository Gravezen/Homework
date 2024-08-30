import pygame
import pygame.threads
import pygame_gui
import random
from functools import reduce
import operator
import math

window_size = (1600, 900)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Пожарник')
pygame.init()

field = pygame.image.load("Поле.png")
field_pos = [50, 50]

rock = pygame.image.load("Камень.png")
rock_pos = [0, 0]

def ramka():
    for i in range(((window_size[0]) // 50)):
        if i == 1:
            rock_pos[0] -= 50
            for j in range ((window_size[1]) // 50):
                window.blit(rock, rock_pos)
                rock_pos[1] += 50
                if j == ((window_size[1]) // 50 - 2):
                    for o in range(((window_size[0]) // 50)):
                        window.blit(rock, rock_pos)
                        rock_pos[0] += 50
            rock_pos[1] = 0
            rock_pos[0] = 0
        elif i == (((window_size[0]) // 50) - 1):
            rock_pos[0] += 50
            for j in range ((window_size[1]) // 50):
                window.blit(rock, rock_pos)
                rock_pos[1] += 50
            rock_pos[1] = 0  
        rock_pos[0] += 50
        window.blit(rock, rock_pos)
        
def random_sdvig(b):
    x = b[0]
    y = b[1]
    a = random.randint(1,5)
    if a == 1:
        x += 50
    if a == 2:
        x -= 50
    if a == 3:
        y += 50
    if a == 4:
        y -= 50
    return [x, y]  

def river(z):
    k = 1
    river_pos = random_coords()
    # window.blit(rive, river_pos)
    a = [random_sdvig(river_pos)]
    while k != z:
        a.append(random_sdvig(a[-1]))
        if 50 < a[-1][0] < 1500 and 50 < a[-1][1] <700:
            # window.blit(rive, a[-1])
            k += 1
    return a


def random_coords():
    x, y = random.randint(100, 1500), random.randint(100, 700)
    if x // 50 and y // 50:
        return x, y

name = ["Речка1.png", "Речка2.png", "Речка3.png", "Речка4.png"]



WHITE = (255, 255, 255)

window.blit(field, field_pos)
ramka()


z = 15
a = river(z)

while True:
    fps = 60
    time_delta = pygame.time.Clock().tick(fps) 
    
    tick = 1

    for i in range(4):
        if time_delta:
            rive = pygame.image.load(name[i])
            for j in range(z):
                window.blit(rive, a[j])    
    
        

    for event in pygame.event.get():



        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    
    

    pygame.display.update()


