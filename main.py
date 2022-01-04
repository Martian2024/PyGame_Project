import pygame
import sys
from Ship import Ship

pygame.font.init()

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
ship = Ship()
fon = pygame.image.load('data\\fon.jpg')
font = pygame.font.Font(None, 50)

def show_progress():
    pygame.draw.rect(screen, pygame.Color('orange'), (75, 515, ship.distance * (1050 / ship.aim_distance), 5))
    pygame.draw.rect(screen, pygame.Color('white'), (75, 515, 1050, 5), 1)

def win():
    text = font.render('YOU WIN!', False, pygame.Color('white'))
    screen.blit(fon, (0, 0))
    screen.blit(text, (550, 250))

while ship.distance < ship.aim_distance:
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
    show_progress()
    pygame.display.update()
    clock.tick(fps)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    win()
    pygame.display.update()
    clock.tick(fps)