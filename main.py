import pygame
import sys
from Ship import Ship
from Farm import Farm
from Lab import Lab

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
ship = Ship()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ship.blt()
    screen.blit(ship.surf, (0, 0))
    pygame.display.update()
    clock.tick(fps)