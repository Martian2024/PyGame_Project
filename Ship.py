import pygame

from Farm import Farm
from Lab import Lab
from Armor import Armor
from PowerPlant import PowerPlant
from MousePointer import MousePointer

class Ship():
    def __init__(self):
        self.map = [['n' for _ in range(30)] for _ in range(15)]
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0,
                          'energy': 100, 'science': 0}
        self.every_single_unit = {'science': [], 'food': [], 'storages': [], 'engines': [], 'energy': [], 'defense': [], 'cabins': [],
                                  'workshops': [], 'armor': []}
        self.group = pygame.sprite.Group()
        self.humans = 10
        self.cell_size = 30
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)), pygame.SRCALPHA)
        self.mouse = MousePointer(0, 0)
        lab = Lab(self, 0, 0)
        farm = Farm(self, 0, 3)
        farm1 = Farm(self, 3, 0)
        lab1 = Lab(self, 5, 3)
        armor = Armor(self, 10, 10)
        plant = PowerPlant(self, 8, 0)
        for i in self.every_single_unit.keys():
            for a in self.every_single_unit[i]:
                self.group.add(a)
        print(self.group.sprites())
        self.lab1 = lab1

    def blt(self):
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)), pygame.SRCALPHA)
        for i in self.every_single_unit.keys():
            for unit in self.every_single_unit[i]:
                unit.new_image()
                self.surf.blit(unit.image, (self.cell_size * unit.x, self.cell_size * unit.y))

    def all_systems_check(self):
        for cat in self.every_single_unit.keys():
            for unit in self.every_single_unit[cat]:
                unit.do()

    def change(self, x, y):
        for unit in self.group.sprites():
            if unit.rect.collidepoint(x, y):
                if unit.working:
                    unit.working = False
                else:
                    unit.working = True