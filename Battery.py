import pygame
from Storages import Storage

class Battery(Storage):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\battery.png'),
                                      pygame.image.load('data\\battery_not_working.png'),
                                      pygame.image.load('data\\battery_broken.png')], 'energy', 0, None)