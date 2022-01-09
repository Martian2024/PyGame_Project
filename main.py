import pygame
import sys
from Ship import Ship
from Buttons import Button, Menu_Button
from MousePointer import MousePointer
from Asteroid import Asteroid
from Engine import  Engine
import random

pygame.font.init()

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
world = pygame.Surface((1200, 600), pygame.SRCALPHA)
world_rect = world.get_rect()
ship = Ship(screen)
fon = pygame.image.load('data\\fon.jpg')
wn = pygame.font.Font(None, 50)
prg = pygame.font.Font(None, 25)
buttons = []
telemetry = Menu_Button(0, 0, pygame.image.load('data\\button_menu.png'), ship)
buttons.append(telemetry)
buttons_group = pygame.sprite.Group(telemetry)
pause = False
mouse_pointer = MousePointer(0, 0)
mouse_traking = False
text_telem = pygame.font.Font(None, 24)
abnormal_blit = 'None'
evnt = 'asteroids'
evnts = ['asteroids', 'failure']
evnt_counter = 0
event_group = pygame.sprite.Group()
motion_x = 0
motion_y = 0


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


def update_world():
    ship.all_systems_check()
    ship.blt()
    screen.blit(ship.surf, (ship.x, ship.y))


def telem():
    screen.fill((95, 205, 228))
    for string in zip([(100, 50), (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (600, 50), (600, 100),
                       (600, 150), (600, 200), (600, 250)], ship.resourses.keys()):
        screen.blit(text_telem.render('{}: {}'.format(string[1], str(ship.resourses[string[1]])), False,
                                      pygame.Color('white')), string[0])


def defeat():
    text = wn.render('YOU\'VE LOST', False, pygame.Color('white'))
    screen.blit(fon, (0, 0))
    screen.blit(text, (550, 250))


def asteroids():
    if random.randint(1, 50) == 1:
        event_group.add(Asteroid(1210, random.randint(10, 590)))
    for i in event_group.sprites():
        i.move()
        if i.rect.topleft[0] < -20:
            i.kill()
        else:
            for a in pygame.sprite.spritecollide(i, ship.group, False):
                a.health -= 6
                i.kill()
    ship.shoot(event_group)
    event_group.draw(screen)


while ship.distance < ship.aim_distance and ship.under_control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                ship.change(event.pos[0], event.pos[1])
            '''elif event.button == 1:
                mouse_pointer.move(*event.pos)
                if pygame.sprite.spritecollide(mouse_pointer, buttons_group, False):
                    pause, abnormal_blit = pygame.sprite.spritecollide(mouse_pointer, buttons_group,
                                                                       False)[0].pressed(pause, abnormal_blit)
                else:
                    mouse_traking = True'''
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_traking = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_traking:
                mouse_pointer.move(*event.pos)
                ship.move(mouse_pointer.x, mouse_pointer.prev_x, mouse_pointer.y, mouse_pointer.prev_y)
                world_rect.move_ip(mouse_pointer.x - mouse_pointer.prev_x, mouse_pointer.y - mouse_pointer.prev_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True
            if event.key == pygame.K_w:
                flag = False
                for i in ship.group:
                    if type(i) == Engine and i.working:
                        flag = True
                if flag:
                    motion_y = -3
            elif event.key == pygame.K_s:
                flag = False
                for i in ship.group:
                    if type(i) == Engine and i.working:
                        flag = True
                if flag:
                    motion_y = 3
            elif event.key == pygame.K_a:
                flag = False
                for i in ship.group:
                    if type(i) == Engine and i.working:
                        flag = True
                if flag:
                    motion_x = -3
            elif event.key == pygame.K_d:
                flag = False
                for i in ship.group:
                    if type(i) == Engine and i.working:
                        flag = True
                if flag:
                    motion_x = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                motion_y = 0
            elif event.key == pygame.K_s:
                motion_y = 0
            elif event.key == pygame.K_a:
                motion_x = 0
            elif event.key == pygame.K_d:
                motion_x = 0
    if ship.comand_module.rect.bottom > screen.get_height() and motion_y > 0:
        motion_y = 0
    elif ship.comand_module.rect.top < 0 and motion_y < 0:
        motion_y = 0
    if ship.comand_module.rect.right > screen.get_width() and motion_x > 0:
        motion_x = 0
    elif ship.comand_module.rect.left < 0 and motion_x < 0:
        motion_x = 0
    ship.move(ship.x + motion_x, ship.x, ship.y + motion_y, ship.y)
    if abnormal_blit == 'None':
        if not pause:
            screen.blit(fon, (0, 0))
            update_world()
            if evnt == None and random.randint(1, 100) == 1:
                evnt = random.choice(evnts)
            if evnt == 'asteroids':
                asteroids()
            evnt_counter += 1

    else:
        if abnormal_blit == 'Telemetry':
            telem()
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
