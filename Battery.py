import pygame
from Storages import Storage


class Battery(Storage):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\battery.png'),
                                      pygame.image.load('data\\battery_not_working.png'),
                                      pygame.image.load('data\\battery_broken.png')],
                         'energy', 0, None, building=building)
        self.charges = {'energy': 0}
        self.max_charges = {'science': 1000}
        self.build_cat = {'Fe': 10, 'Cu': 10}

    def do(self):
        if self.health < self.max_health // 2:
            self.working = False
            self.broken = True
        self.new_image()
