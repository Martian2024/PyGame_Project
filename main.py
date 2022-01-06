import pygame
import sys
from Ship import Ship
from Buttons import Button, Menu_Button
from MousePointer import MousePointer

pygame.font.init()

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
ship = Ship()
fon = pygame.image.load('data\\fon.jpg')
wn = pygame.font.Font(None, 50)
prg = pygame.font.Font(None, 25)
buttons = []
telemetry = Menu_Button(0, 0, pygame.image.load('data\\button_menu.png'), ship)
buttons.append(telemetry)
buttons_group = pygame.sprite.Group(telemetry)
abnormal_blit = False
pause = False
mouse_pointer = MousePointer(0, 0)
mouse_traking = False

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

def defeat():
    text = wn.render('YOU\'VE LOST', False, pygame.Color('white'))
    screen.blit(fon, (0, 0))
    screen.blit(text, (550, 250))

while ship.distance < ship.aim_distance and ship.under_control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                ship.change(event.pos[0] - 150, event.pos[1] - 75)
            elif event.button == 1:
                mouse_pointer.move(*event.pos)
                if pygame.sprite.spritecollide(mouse_pointer, buttons_group, False):
                    pass
                else:
                    mouse_traking = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_traking = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_traking:
                mouse_pointer.prev_x = mouse_pointer.x
                mouse_pointer.prev_y = mouse_pointer.y
                mouse_pointer.x = event.pos[0]
                mouse_pointer.y = event.pos[1]
                ship.move(mouse_pointer.x, mouse_pointer.prev_x, mouse_pointer.y, mouse_pointer.prev_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True
    if not pause:
        ship.all_systems_check()
        ship.blt()
    screen.blit(fon, (0, 0))
    screen.blit(ship.surf, (ship.x, ship.y))
    show_progress()
    show_buttons()
    pygame.display.update()
    clock.tick(fps)
if ship.under_control:
    win()
else:
    defeat()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(fps)