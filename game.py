import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

screen = pygame.display.set_mode((900, 400), 0, 32)

background_filename = 'imagens/fundo.jpg'
background = pygame.image.load(background_filename).convert()

ship = {
    'surface': pygame.image.load('imagens/ship.png').convert_alpha()
    'position': [randrange(900), randrange(400)],
    'speed': {
        'x': 0,
        'y': 0
    }
}

pygame.display.set_caption('Asteroides')

clock = pygame.time.Clock()


def create_asteroid():
    return {
        'surface': pygame.image.load('imagens/asteroid.png').convert_alpha(),
        'position': [randrange(892), -64],
        'speed': randrange(1, 11)
    }

ticks_to_asteroid = 90
asteroids = []


def move_asteroids():
    for asteroid in asteroids:
        asteroid['position'][1] += asteroid['speed']


def remove_used_asteroids():
    for asteroid in asteroids:
        if asteroid['position'][1] > 560:
            asteroids.remove(asteroid)


def get_rect(obj):
    return Rect(obj['position'][0],
                obj['position'][1],
                obj['surface'].get_width(),
                obj['surface'].get_height())


def ship_collided():
    ship_rect = get_rect(ship)
    for asteroid in asteroids:
        if ship_rect.colliderect(get_rect(asteroid)):
            return True
    return False

collided = False

while True:

    if not ticks_to_asteroid:
        ticks_to_asteroid = 90
        asteroids.append(create_asteroid())
    else:
        ticks_to_asteroid -= 1

    ship['speed'] = {
        'x': 0,
        'y': 0
    }

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        ship['speed']['y'] = -5
    elif pressed_keys[K_DOWN]:
        ship['speed']['y'] = 5

    if pressed_keys[K_LEFT]:
        ship['speed']['x'] = -5
    elif pressed_keys[K_RIGHT]:
        ship['speed']['x'] = 5

    screen.blit(background, (0, 0))

    if not collided:
        collided = ship_collided()
        ship['position'][0] += ship['speed']['x']
        ship['position'][1] += ship['speed']['y']

        screen.blit(ship['surface'], ship['position'])

    move_asteroids()

    for asteroid in asteroids:
        screen.blit(asteroid['surface'], asteroid['position'])

    pygame.display.update()
    time_passed = clock.tick(30)

    remove_used_asteroids()
