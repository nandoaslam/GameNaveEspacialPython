import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((900, 400), 0, 32)

background_file = 'imagens/fundo.jpg'
background = pygame.image.load(background_file).convert()
jogando = True

ship_filename = 'imagens/nave.png'
ship = pygame.image.load(ship_filename).convert_alpha()

pygame.display.set_caption('Nave Espacial')

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(ship, (400,300))
    pygame.display.update()
    time_passed = clock.tick(30)
