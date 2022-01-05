import pygame
import sys
from Ship import Ship
from Buttons import Button, Menu_Button

pygame.font.init()

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
ship = Ship()
fon = pygame.image.load('data\\fon.jpg')
wn = pygame.font.Font(None, 50)
prg = pygame.font.Font(None, 25)
buttons = []
telemetry = Menu_Button(0, 0, pygame.image.load('data\\button_menu.png'))
buttons.append(telemetry)

def show_buttons():
    for button in buttons:
        screen.blit(button.image, (button.x, button.y))

def show_progress():
    st = prg.render('start', True, pygame.Color('white'))
    screen.blit(st, (65, 520))
    fn = prg.render('finish', True, pygame.Color('white'))
    screen.blit(fn, (1110, 520))
    pygame.draw.rect(screen, pygame.Color('orange'), (75, 515, ship.distance * (1050 / ship.aim_distance), 5))
    pygame.draw.rect(screen, pygame.Color('white'), (75, 515, 1050, 5), 1)

def win():
    text = wn.render('YOU WIN!', False, pygame.Color('white'))
    screen.blit(fon, (0, 0))
    screen.blit(text, (550, 250))

while ship.distance < ship.aim_distance and ship.under_control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                ship.change(event.pos[0] - 150, event.pos[1] - 75)
            elif event.button == 1:
                if ship.surf.get_rect().collidepoint(*event.pos):
                    pass
                else:
                    for button in buttons:
                        if button.rect.collidepoint(*event.pos):
                            button.pressed()
    ship.all_systems_check()
    ship.blt()
    screen.blit(fon, (0, 0))
    screen.blit(ship.surf, (150, 75))
    show_progress()
    show_buttons()
    pygame.display.update()
    clock.tick(fps)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    win()
    pygame.display.update()
    clock.tick(fps)