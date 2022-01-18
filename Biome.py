import pygame

from  Unit import Unit

class Biome(Unit):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\biome.png'),
                                      pygame.image.load('data\\biome_not_working.png'),
                                      pygame.image.load('data\\biome_broken.png')], 'cabins', 10, ['O2', 'food'],
                         building=building)
        self.max_health = 10
        self.charge = 10000
        self.max_charge = 10000
        self.health = 10
        self.build_cat = {'Fe': 10, 'Cu': 20, 'Si': 10, 'Al': 5, 'H2O': 5, }

    def input(self):
        try:
            if self.working:
                if self.charge + self.ship.humans // len(
                        list(filter(lambda x: x.working, self.ship.every_single_unit['cabins']))) <= self.max_charge:
                    self.charge += self.ship.humans // len(
                        list(filter(lambda x: x.working, self.ship.every_single_unit['cabins'])))
                else:
                    self.charge = self.max_charge
        except ZeroDivisionError:
            self.charge = 0

    def output(self):
        if self.working:
            self.ship.humans += self.charge
            self.charge = 0

    def do(self):
        if self.health < self.max_health // 2:
            self.broken = True
            self.working = False
        if self.working:
            flag = True
            for i in self.consume_cat:
                if self.ship.resourses[i] < self.consume:
                    flag = False
                else:
                    self.ship.resourses[i] -= self.consume
            if flag:
                self.ship.resourses['CO2'] += 6
            else:
                self.working = False

        self.new_image()