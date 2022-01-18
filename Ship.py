import pygame
import random

from Farm import Farm
from Lab import Lab
from Armor import Armor
from PowerPlant import PowerPlant
from Battery import Battery
from Engine import Engine
from Command_module import Comand_Module
from Warehouse import Warehouse
from Laser import Laser
from Biome import Biome
from Asteroid import Asteroid
from Container import Container


class Ship():
    def __init__(self, screen):
        self.x = 150
        self.y = 75
        self.distance = 0
        self.aim_distance = 1000000
        self.velocity = 10
        self.under_control = True
        self.map = [['n' for _ in range(30)] for _ in range(14)]
        self.resourses = {'Fe': 100, 'Cu': 50, 'O2': 50, 'CO2': 50, 'Al': 50, 'Si': 50, 'U': 50, 'H2O': 50,
                          'food': 50, 'energy': 0, 'science': 0}
        self.every_single_unit = {'energy': [], 'commands': [], 'food': [], 'storages': [], 'engines': [],
                                  'science': [], 'defense': [], 'cabins': [],
                                  'armor': []}
        self.storages = {'energy': [], 'science': [], 'storages': []}
        self.group = pygame.sprite.Group()
        self.cannons = []
        self.comand_modules = []
        self.humans = 10
        self.cell_size = 30
        self.screen = screen
        eng = Engine(self, 14, 7)
        eng1 = Engine(self, 14, 9)
        plant1 = PowerPlant(self, 18, 7)
        plant2 = PowerPlant(self, 18, 9)
        self.comand_module = Comand_Module(self, 16, 11)
        bat1 = Battery(self, 20, 7)
        bat2 = Battery(self, 20, 9)
        biome1 = Biome(self, 22, 7)
        biome2 = Biome(self, 22, 9)
        lab1 = Lab(self, 17, 6)
        farm = Farm(self, 24, 7)
        ware = Warehouse(self, 20, 6)
        ware.charges = {'Fe': 10000, 'Cu': 10000, 'O2': 10000, 'CO2': 10000, 'Al': 10000, 'Si': 10000, 'U': 10000,
                        'H2O': 10000, 'food': 10000}
        arm = Armor(self, 23, 6)
        arm = Armor(self, 23, 7)
        arm = Armor(self, 23, 8)
        laser1 = Laser(self, 3, 1)
        laser2 = Laser(self, 8, 12)
        for i in self.every_single_unit.keys():
            for a in self.every_single_unit[i]:
                self.group.add(a)
        for i in self.storages.keys():
            for unit in self.storages[i]:
                unit.input()
        self.new_group = pygame.sprite.Group()
        self.new_group.add(self.comand_module)
        self.storages_types = [Battery, Lab]

    def destroy(self, unit):
        self.group.remove(unit)
        self.every_single_unit[unit.cat].remove(unit)
        if type(unit) in self.storages_types:
            self.storages[unit.cat].remove(unit)
        unit.working = False

    def dfs(self, sprite, visited):
        visited.append(sprite)
        for i in pygame.sprite.spritecollide(sprite, self.group, False):
            if i not in visited:
                self.new_group.add(i)
                self.dfs(i, visited)

    def blt(self):
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)), pygame.SRCALPHA)
        for i in self.every_single_unit.keys():
            for unit in self.every_single_unit[i]:
                unit.new_image()
        self.group.draw(self.screen)


    def all_systems_check(self):
        for i in self.group.sprites():
            if i.health <= 0:
                self.destroy(i)
        self.dfs(self.comand_module, [])
        for unit in self.group:
            if unit not in self.new_group.sprites():
                self.destroy(unit)
        self.new_group = pygame.sprite.Group()
        self.new_group.add(self.comand_module)
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0,
                          'food': 0, 'energy': 0, 'science': 0}
        self.humans = 0
        for i in self.every_single_unit['cabins']:
            i.output()
        for i in self.storages.keys():
            for unit in self.storages[i]:
                unit.output()
        self.under_control = False
        for i in self.comand_modules:
            if i.working:
                self.under_control = True
        for cat in self.every_single_unit.keys():
            for unit in self.every_single_unit[cat]:
                unit.do()
        for i in self.storages.keys():
            for unit in self.storages[i]:
                unit.input()
        for i in self.every_single_unit['cabins']:
            i.input()

    def change(self, x, y):
        for unit in self.group.sprites():
            if unit.rect.collidepoint(x, y):
                if unit.working:
                    unit.working = False
                else:
                    unit.working = True

    def move(self, nx, ox, ny, oy):
        self.x = nx
        self.y = ny
        for cat in self.every_single_unit.keys():
            for unit in self.every_single_unit[cat]:
                unit.rect.move_ip(nx - ox, ny - oy)


    def shoot(self, event_group):
        for cannon in self.cannons:
            if pygame.sprite.spritecollideany(cannon, event_group, pygame.sprite.collide_circle_ratio(3.5)) != None:
                for i in [pygame.sprite.spritecollideany(cannon, event_group, pygame.sprite.collide_circle_ratio(3.5))]:
                    if type(i) == Asteroid:
                        cannon.shoot(i)
                    elif type(i) == Container:
                        cannon.grab(i)
                        for i in self.resourses.keys():
                            self.resourses[i] += random.randint(100, 100)