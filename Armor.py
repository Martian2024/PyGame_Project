import pygame
from Unit import Unit

class Armor(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\armor_ok.png'), pygame.image.load('data\\armor_ok.png'),
                                      pygame.image.load('data\\armor_damaged.png')], 'armor', 0, None)
        self.health = 100
        self.max_haelth = 100

    def do(self):
        pass