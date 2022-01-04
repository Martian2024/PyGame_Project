import pygame

from Farm import Farm
from Lab import Lab
from Armor import Armor
from PowerPlant import PowerPlant
from Battery import Battery
from Engine import Engine

class Ship():
    def __init__(self):
        self.distance = 0
        self.aim_distance = 1000
        self.velocity = 0
        self.map = [['n' for _ in range(30)] for _ in range(15)]
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0,
                          'energy': 100, 'science': 0}
        self.every_single_unit = {'science': [], 'food': [], 'storages': [], 'engines': [], 'energy': [], 'defense': [], 'cabins': [],
                                  'workshops': [], 'armor': []}
        self.storages = {'energy': []}
        self.group = pygame.sprite.Group()
        self.humans = 10
        self.cell_size = 30
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)), pygame.SRCALPHA)
        lab = Lab(self, 0, 0)
        farm = Farm(self, 0, 3)
        farm1 = Farm(self, 3, 0)
        lab1 = Lab(self, 5, 3)
        armor = Armor(self, 10, 10)
        plant = PowerPlant(self, 8, 0)
        battery = Battery(self, 10, 10)
        battery1 = Battery(self, 8, 3)
        eng = Engine(self, 11, 0)
        for i in self.every_single_unit.keys():
            for a in self.every_single_unit[i]:
                self.group.add(a)

    def blt(self):
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)), pygame.SRCALPHA)
        for i in self.every_single_unit.keys():
            for unit in self.every_single_unit[i]:
                unit.new_image()
                self.surf.blit(unit.image, (self.cell_size * unit.x, self.cell_size * unit.y))

    def all_systems_check(self):
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0,
                          'energy': 0, 'science': 0}
        for cat in self.storages.keys():
            for unit in self.storages[cat]:
                unit.output()
        for cat in self.every_single_unit.keys():
            for unit in self.every_single_unit[cat]:
                unit.do()
        for cat in self.storages.keys():
            for unit in self.storages[cat]:
                unit.input()


    def change(self, x, y):
        for unit in self.group.sprites():
            if unit.rect.collidepoint(x, y):
                if unit.working:
                    unit.working = False
                else:
                    unit.working = True