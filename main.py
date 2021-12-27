import pygame
import sys

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()
    clock.tick(fps)