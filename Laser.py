import random

import pygame
from Unit import Unit


class Laser(Unit):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\Laser1.png'),
                                      pygame.image.load('data\\Laser2.png'),
                                      pygame.image.load('data\\Laser_not_working.png'),
                                      pygame.image.load('data\\Laser_broken.png')],
                         'armor', 10, ['energy'], building=building)
        self.cooldown = 0
        self.ship.cannons.append(self)
        self.build_cat = {'Fe': 10, 'Cu': 5}

    def do(self):
        if self.health < self.max_health // 2:
            self.broken = True
            self.working = False
        self.new_image()

    def shoot(self, ast):
        if self.working:
            if self.cooldown == 0:
                pygame.draw.line(self.ship.screen, (0, 211, 255), self.rect.center, ast.rect.center, 5)
                ast.kill()
                self.cooldown += 1
            if 0 < self.cooldown < 15:
                self.cooldown += 1
            else:
                self.cooldown = 0

    def grab(self, cont):
        if self.working and not self.broken:
            if self.cooldown == 0:
                pygame.draw.line(self.ship.screen, pygame.Color('yellow'), self.rect.center, cont.rect.center, 5)
                pygame.draw.circle(self.ship.screen, pygame.Color('yellow'), cont.rect.center, 30)
                cont.kill()
                self.cooldown += 1
            if 0 < self.cooldown < 15:
                self.cooldown += 1
            else:
                self.cooldown = 0

    def build(self, x, y):
        super().build(x, y)
        for i in self.build_cat.keys():
            self.ship.resourses[i] -= self.build_cat[i]