import pygame
from Unit import Unit

class Armor(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\armor_ok.png'), pygame.image.load('data\\armor_ok.png'),
                                      pygame.image.load('data\\armor_damaged.png')], 'armor', 0, None)

    def do(self):
        pass