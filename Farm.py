import pygame
from Unit import Unit

class Farm(Unit):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\farm.png'), pygame.image.load('data\\farm_not_working.png'),
                                      pygame.image.load('data\\farm_broken.png')],
                         'food', 3, ['energy', 'CO2'], building=building)
        self.health = 10
        self.max_health = 10
        self.build_cat = {'Fe': 10, 'Cu': 5, 'Si': 7}
        self.producing_cat = {'food': 5, 'O2': 5}


    def new_image(self):
        if self.broken:
            self.image = self.image_broken
        elif not self.working:
            self.image = self.image_not_working
        else:
            self.image = self.image_working

    def do(self):
        if self.health < self.max_health // 2:
            self.working = False
            self.broken = True
        if self.working:
            for cat in self.consume_cat:
                if self.ship.resourses[cat] < self.consume:
                    self.working = False
                else:
                    self.ship.resourses[cat] -= self.consume
            if self.working:
                for cat in self.producing_cat.keys():
                    self.ship.resourses[cat] += self.producing_cat[cat]
        self.new_image()