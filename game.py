import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

screen = pygame.display.set_mode((900, 400), 0, 32)

background_file = 'imagens/fundo.jpg'
background = pygame.image.load(background_file).convert()

ship_filename = 'imagens/nave.png'
ship = pygame.image.load(ship_filename).convert_alpha()
nave_position = [randrange(900), randrange(400)]

"""speed = {
    'x': 0,
    'y': 0
    }"""


pygame.display.set_caption('Nave Espacial')

clock = pygame.time.Clock()
while True:
    speed = {
        'x': 0,
        'y': 0
    }
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        speed['y'] = -5
    elif pressed_keys[K_DOWN]:
        speed['y'] = 5
    if pressed_keys[K_LEFT]:
        speed['x'] = -5
    elif pressed_keys[K_RIGHT]:
        speed['x'] = 5

    screen.blit(background, (0, 0))
    nave_position[0] += speed ['x']
    nave_position[1] += speed ['y']
    screen.blit(ship, nave_position)
    pygame.display.update()
    time_passed = clock.tick(30)
