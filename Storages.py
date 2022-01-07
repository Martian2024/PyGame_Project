import pygame
from Unit import Unit

class Storage(Unit):
    def __init__(self, ship, x, y, images, cat, consume, consume_cat):
        super().__init__(ship, x, y, images, cat, consume, consume_cat)
        self.max_charge = 10
        self.charge = 0
        self.ship.storages[self.cat].append(self)
        self.health = 10

    def output(self):
        if self.working:
            self.ship.resourses[self.cat] += self.charge
            self.charge = 0

    def input(self):
        try:
            if self.working:
                if self.charge + self.ship.resourses[self.cat] // len(list(filter(lambda x: x.working, self.ship.storages[self.cat]))) <= self.max_charge:
                    self.charge += self.ship.resourses[self.cat] // len(list(filter(lambda x: x.working, self.ship.storages[self.cat])))
                else:
                    self.charge = self.max_charge
        except ZeroDivisionError:
            self.charge = 0

    def do(self):
        pass