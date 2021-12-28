import pygame

from Farm import Farm
from Lab import Lab

class Ship():
    def __init__(self):
        self.map = [['n' for _ in range(60)] for _ in range(30)]
        self.resourses = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0,
                          'energy': 0}
        self.every_single_unit = {'labs': [], 'farms': [], 'storages': [], 'engines': [], 'energy': [], 'defense': [], 'cabins': [],
                                  'workshops': []}
        self.group = pygame.sprite.Group()
        for i in self.every_single_unit.keys():
            for a in range(len(self.every_single_unit[i])):
                self.group.add(self.every_single_unit[i][a])
        self.humans = 10
        self.cell_size = 30
        self.surf = pygame.Surface((self.cell_size * len(self.map[0]), self.cell_size * len(self.map)))
        lab = Lab(self, 0, 0)
        farm = Farm(self, 0, 3)
        farm1 = Farm(self, 10, 10)


    def blt(self):
        self.surf.fill((0, 0, 0))
        for i in self.every_single_unit.keys():
            for unit in self.every_single_unit[i]:
                self.surf.blit(unit.image, (self.cell_size * unit.x, self.cell_size * unit.y))
