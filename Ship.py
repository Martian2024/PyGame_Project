import pygame

from Farm import Farm
from Lab import Lab
from Armor import Armor
from PowerPlant import PowerPlant
from Battery import Battery
from Engine import Engine
from Command_module import Comand_Module

class Ship():
    def __init__(self):
        self.distance = 0
        self.aim_distance = 1000000
        self.velocity = 10
        self.under_control = True
        self.controls = []
        self.map = [['n' for _ in range(30)] for _ in range(15)]
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0,
                          'energy': 100, 'science': 0}
        self.every_single_unit = {'energy': [], 'commands': [], 'food': [], 'storages': [], 'engines': [], 'science': [], 'defense': [], 'cabins': [],
                                  'workshops': [], 'armor': []}
        self.storages = {'energy': []}
        self.group = pygame.sprite.Group()
        self.humans = 10
        self.cell_size = 30
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)), pygame.SRCALPHA)
        eng = Engine(self, 0, 6)
        plant1 = PowerPlant(self, 8, 6)
        plant2 = PowerPlant(self, 11, 6)
        self.comand_module = Comand_Module(self, 14, 6)
        bat1 = Battery(self, 8, 3)
        bat2 = Battery(self, 8, 9)
        farm1 = Farm(self, 11, 3)
        farm2 = Farm(self, 11, 9)
        lab1 = Lab(self, 17, 6)
        for i in self.every_single_unit.keys():
            for a in self.every_single_unit[i]:
                self.group.add(a)
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
                self.surf.blit(unit.image, (self.cell_size * unit.x, self.cell_size * unit.y))

    def all_systems_check(self):
        for i in self.group.sprites():
            if i.health == 0:
                self.destroy(i)
        self.dfs(self.comand_module, [])
        for unit in self.group:
            if unit not in self.new_group.sprites():
                self.destroy(unit)
        self.new_group = pygame.sprite.Group()
        self.new_group.add(self.comand_module)
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0,
                          'energy': 0, 'science': 0}
        for i in self.storages.keys():
            for unit in self.storages[i]:
                unit.output()
        flag = False
        for unit in self.controls:
            if unit.working:
                flag = True
        if not flag:
            self.under_control = False
        for cat in self.every_single_unit.keys():
            for unit in self.every_single_unit[cat]:
                unit.do()
        for i in self.storages.keys():
            for unit in self.storages[i]:
                unit.input()


    def change(self, x, y):
        for unit in self.group.sprites():
            if unit.rect.collidepoint(x, y):
                if unit.working:
                    unit.working = False
                else:
                    unit.working = True