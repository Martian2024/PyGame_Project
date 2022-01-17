import pygame
from Unit import Unit

class Armor(Unit):
    def __init__(self, ship, x, y, building=False):
        super().__init__(ship, x, y, [pygame.image.load('data\\armor_ok.png'), pygame.image.load('data\\armor_ok.png'),
                                          pygame.image.load('data\\armor_damaged.png')], 'armor', 0, None,
                         building=building)
        self.health = 10
        self.max_haelth = 10

    def do(self):
        if self.health < self.max_health // 2:
            self.broken = True
            self.working = False
        self.new_image()