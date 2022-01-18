import pygame

from Storages import Storage

class Warehouse(Storage):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\storage.png'), pygame.image.load('data\\storage.png'),
                                      pygame.image.load('data\\storage.png')],
                         'storages', 0, None,  building=building)
        self.charges = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0}
        self.max_charges = {'Fe': 10000, 'Cu': 10000, 'O2': 10000, 'CO2': 10000, 'Al': 10000, 'Si': 10000, 'U': 10000,
                            'H2O': 10000, 'food': 10000}
        self.build_cat = {'Fe': 10, 'Cu': 2}

    def output(self):
        if self.working:
            for cat in self.charges.keys():
                self.ship.resourses[cat] += self.charges[cat]
                self.charges[cat] = 0

    def input(self):
        if self.working:
            try:
                for cat in self.charges.keys():
                    if self.charges[cat] + self.ship.resourses[cat] // len(list(filter(lambda x: x.working, self.ship.storages[self.cat]))) <= self.max_charges[cat]:
                        self.charges[cat] += self.ship.resourses[cat] // len(list(filter(lambda x: x.working, self.ship.storages[self.cat])))
                    else:
                        self.charges[cat] = self.max_charges[cat]
            except ZeroDivisionError:
                self.charges = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0}
