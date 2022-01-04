import pygame
import sys
from Ship import Ship

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
ship = Ship()
fon = pygame.image.load('data\\fon.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                ship.change(event.pos[0] - 150, event.pos[1] - 75)
    ship.all_systems_check()
    ship.blt()
    screen.blit(fon, (0, 0))
    screen.blit(ship.surf, (150, 75))
    pygame.display.update()
    clock.tick(fps)