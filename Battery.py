import pygame
from Unit import Unit

class Battery(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\battery.png'),
                                      pygame.image.load('data\\battery_not_working.png'),
                                      pygame.image.load('data\\battery_broken.png')], 'energy', 0, None)
        self.max_charge = 10
        self.charge = 0
        self.ship.storages[self.cat].append(self)
        self.health = 10

    def output(self):
        if self.working:
            self.ship.resourses['energy'] += self.charge
            self.charge = 0

    def input(self):
        try:
            self.charge += self.ship.resourses['energy'] // len(list(filter(lambda x: x.working, self.ship.storages['energy'])))
        except ZeroDivisionError:
            self.charge = 0

    def do(self):
        pass