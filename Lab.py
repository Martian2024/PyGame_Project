import pygame
from Storages import Storage


class Lab(Storage):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y,
                         [pygame.image.load('data\\lab1.png'), pygame.image.load('data\\lab2.png'),
                          pygame.image.load('data\\lab_not_working.png'), pygame.image.load('data\\lab_broken.png')],
                         'science', 3, ['energy'], building=building)
        self.health = 10
        self.max_health = 10
        self.min_workers = 20
        self.workers = 0
        self.max_workers = 1000
        self.charges = {'science': 0}
        self.max_charges = {'science': 100}
        self.built_cat = {'Fe': 10, 'Cu': 20, 'Si': 10, 'Al': 5, 'U': 5}

    def do(self):
        if self.health < self.max_health // 2:
            self.working = False
            self.broken = True
        if self.working:
            if self.ship.resourses['energy'] >= 3 and self.ship.humans != 0:
                self.ship.resourses['science'] += 3 * self.ship.humans // len(list(filter(lambda x: x.working, self.ship.storages['science']))) // self.max_workers * self.max_workers * 0.005
                self.ship.resourses['energy'] -= 3 * self.workers * self.ship.humans // \
                                                  len(list(
                                                      filter(lambda x: x.working, self.ship.storages['science']))) // \
                                                  self.max_workers * self.max_workers * 0.01
            else:
                self.working = False
        self.new_image()

    def build(self, x, y):
        super().build(x, y)
        self.ship.storages.append(self)
