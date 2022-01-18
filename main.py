import pygame
import sys
import pygame_gui
from pygame_gui.core import ObjectID
from Ui import *
from Ship import Ship
from MousePointer import MousePointer
from Asteroid import Asteroid
from Container import Container
from Laser import Laser
from Lab import Lab
from PowerPlant import PowerPlant
from Farm import Farm
from Command_module import Comand_Module
from Storages import Storage
from Engine import Engine
from Battery import Battery
from Armor import Armor
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1200, 600))
world = pygame.Surface((1200, 600), pygame.SRCALPHA)
world_rect = world.get_rect()
ship = Ship(screen)
fon = pygame.image.load('data\\fon.jpg')
wn = pygame.font.Font(None, 50)
progrs = pygame.font.Font(None, 25)
pause = False
mouse_pointer = MousePointer(0, 0)
mouse_traking = False
evnt = None
evnts = ['asteroids', 'asteroids', None, 'failure']
evnt_counter = 0
event_group = pygame.sprite.Group()
motion_x = 0
motion_y = 0
manager = pygame_gui.UIManager((1200, 600), 'ui.json')
building = False
can_build = True
resourses_wind = Resourses_window(200, 100, manager)
building_wind = Building_window(200, 100, manager)
tel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (30, 30)),
                                   text='',
                                   manager=manager, object_id=ObjectID(object_id='#telemetry'))
build = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 0), (30, 30)),
                                     text='',
                                     manager=manager, object_id=ObjectID(object_id='#building_button'))
'''tip = pygame_gui.elements.UITooltip(html_text='tooltip', hover_distance=0, manager=manager,
                                                     parent_element=build)'''
building_module = None


def show_progress():
    st = progrs.render('start', True, pygame.Color('white'))
    screen.blit(st, (65, 520))
    fn = progrs.render('finish', True, pygame.Color('white'))
    screen.blit(fn, (1110, 520))
    if evnt == None:
        danger = progrs.render('Danger: you\'re in deep space, bro...', True, pygame.Color('white'))
    else:
        danger = progrs.render('Danger: {}'.format(evnt), True, pygame.Color('white'))
    screen.blit(danger, (65, 550))
    pygame.draw.rect(screen, pygame.Color('orange'), (75, 515, ship.distance * (1050 / ship.aim_distance), 5))
    pygame.draw.rect(screen, pygame.Color('white'), (75, 515, 1050, 5), 1)


def win():
    text = wn.render('YOU WIN!', False, pygame.Color('white'))
    screen.blit(fon, (0, 0))
    screen.blit(text, (550, 250))


def update_world():
    event_group.draw(screen)
    ship.blt()
    screen.blit(ship.surf, (ship.x, ship.y))


def defeat():
    text = wn.render('YOU\'VE LOST', False, pygame.Color('white'))
    screen.blit(fon, (0, 0))
    screen.blit(text, (550, 250))


def asteroids():
    if random.randint(1, int(100 / current_dif)) == 1 and evnt_counter < 500:
        event_group.add(Asteroid(1210, random.randint(10, 590), current_dif))
    for i in event_group.sprites():
        if i.rect.topleft[0] < -20:
            i.kill()
        else:
            for a in pygame.sprite.spritecollide(i, ship.group, False):
                a.health -= 6
                i.kill()


while ship.distance < ship.aim_distance and ship.under_control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                ship.change(event.pos[0], event.pos[1])
            elif event.button == 1:
                mouse_pointer.move(*event.pos)
                if building:
                    if can_build:
                        res = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0,
                          'food': 0, 'energy': 0, 'science': 0}
                        for unit in ship.storages['storages']:
                            for i in unit.charges.keys():
                                res[i] += unit.charges[i]
                        for i in building_module.build_cat.keys():
                            if res[i] < building_module.build_cat[i]:
                                can_build = False
                        if can_build:

                            for unit in ship.storages['storages']:
                                for cat in building_module.build_cat.keys():
                                    try:
                                        unit.charges[cat] -= \
                                            building_module.build_cat[cat] // \
                                            len(list(filter(lambda x: x.working, ship.storages['storages'])))
                                        building_module.build(mouse_pointer.x,
                                                              mouse_pointer.y)
                                        building = False
                                        pause = False
                                        mouse_traking = False
                                    except ZeroDivisionError:
                                        pass

        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            if mouse_traking and building:
                mouse_pointer.move(*event.pos)
                building_module.rect.topleft = (event.pos[0] // ship.cell_size * ship.cell_size,
                                                   event.pos[1] // ship.cell_size * ship.cell_size)
                can_build = True
                for i in ship.group.sprites():
                    if pygame.Rect(building_module.rect.left - 1, building_module.rect.top - 1,
                                   building_module.rect.width + 2,
                                   building_module.rect.height + 2).colliderect(pygame.Rect(i.rect.left + 4,
                                                                                            i.rect.top + 4,
                                                                                            i.rect.width - 8,
                                                                                            i.rect.height - 8)):
                        can_build = False
            elif mouse_traking:
                mouse_pointer.move(*event.pos)
                ship.move(mouse_pointer.x, mouse_pointer.prev_x, mouse_pointer.y, mouse_pointer.prev_y)
                world_rect.move_ip(mouse_pointer.x - mouse_pointer.prev_x, mouse_pointer.y - mouse_pointer.prev_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if building:
                    building = False
                    pause = False
                    mouse_traking = False
                elif pause:
                    pause = False
                elif not pause:
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
            elif event.key == pygame.K_ESCAPE:
                building = False
                pause = False
                mouse_traking = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                motion_y = 0
            elif event.key == pygame.K_s:
                motion_y = 0
            elif event.key == pygame.K_a:
                motion_x = 0
            elif event.key == pygame.K_d:
                motion_x = 0
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == tel:
                resourses_wind.show_telem(ship)
                pause = True
            elif type(event.ui_element) == Close_Button:
                event.ui_element.close()
            elif event.ui_element == build:
                pause = True
                building_wind.show()
            elif type(event.ui_element) == Building_Button:
                pause = True
                building = True
                mouse_traking = True
                building_wind.hide()
                ship.move(0, ship.x, 0, ship.y)
                if event.ui_object_id == '#building_window.#panel_container.#battery_button':
                    building_module = Battery(ship, 0, 0, building=True)
                elif event.ui_object_id == '#building_window.#panel_container.#engine_button':
                    building_module = Engine(ship, 0, 0, building=True)
                elif event.ui_object_id == '#building_window.#panel_container.#lab_button':
                    building_module = Lab(ship, 0, 0, building=True)
                elif event.ui_object_id == '#building_window.#panel_container.#powerplant_button':
                    building_module = PowerPlant(ship, 0, 0, building=True)
                elif event.ui_object_id == '#building_window.#panel_container.#farm_button':
                    building_module = Farm(ship, 0, 0, building=True)
                elif event.ui_object_id == '#building_window.#panel_container.#laser_button':
                    building_module = Laser(ship, 0, 0, building=True)
                elif event.ui_object_id == '#building_window.#panel_container.#armor_button':
                    building_module = Armor(ship, 0, 0, building=True)
                building_module.rect.topleft = (mouse_pointer.x // ship.cell_size * ship.cell_size,
                                                   mouse_pointer.y // ship.cell_size * ship.cell_size)
        manager.process_events(event)
    manager.update(0)
    if ship.comand_module.rect.bottom > screen.get_height() and motion_y > 0:
        motion_y = 0
    elif ship.comand_module.rect.top < 0 and motion_y < 0:
        motion_y = 0
    if ship.comand_module.rect.right > screen.get_width() and motion_x > 0:
        motion_x = 0
    elif ship.comand_module.rect.left < 0 and motion_x < 0:
        motion_x = 0
    screen.blit(fon, (0, 0))
    if not pause:
        current_dif = ship.distance / ship.aim_distance
        ship.move(ship.x + motion_x, ship.x, ship.y + motion_y, ship.y)
        for i in event_group.sprites():
            i.move()
        ship.all_systems_check()
        ship.shoot(event_group)
        if random.randint(1, 1000) == 1:
            event_group.add(Container(1210, random.randint(10, 590)))
        if evnt == None and random.randint(1, 10) == 1 and evnt_counter > 1000 and ship.distance < 950000:
            evnt = random.choice(evnts)
            evnt_counter = 0
        if evnt == 'asteroids':
            asteroids()
        elif evnt == 'failure':
            unit = random.choice(ship.group.sprites())
            while type(unit) == Comand_Module:
                unit = random.choice(ship.group.sprites())
            unit.broken = True
            unit.working = False
            evnt_counter = 999
        evnt_counter += 1
        if evnt_counter == 1000:
            evnt = None
    else:
        screen.blit(pygame.font.Font(None, 35).render('PAUSE', False, pygame.Color('white')), (550, 550))
    update_world()
    if building:
        if not can_build:
            building_module.image = pygame.Surface((building_module.rect.width, building_module.rect.height),
                                                   pygame.SRCALPHA)
            building_module.image.fill(pygame.Color('red'))
        else:
            building_module.image = building_module.images[0]
        screen.blit(building_module.image,
                        (mouse_pointer.x // ship.cell_size * ship.cell_size - 1,
                         mouse_pointer.y // ship.cell_size * ship.cell_size - 1))
    show_progress()
    manager.draw_ui(screen)
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
