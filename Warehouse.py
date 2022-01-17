import pygame

from Storages import Storage

class Warehouse(Storage):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\storage.png'), pygame.image.load('data\\storage.png'),
                                      pygame.image.load('data\\storage.png')],
                         'storages', 0, None,  building=building)
        self.charges = {'Fe': 0, 'Cu': 0, 'O2': 0, 'CO2': 0, 'Al': 0, 'Si': 0, 'U': 0, 'H2O': 0, 'food': 0}
        self.max_charges = {'Fe': 100, 'Cu': 100, 'O2': 100, 'CO2': 100, 'Al': 100, 'Si': 100, 'U': 100, 'H2O': 100,
                            'food': 100}
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
