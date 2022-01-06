import pygame
from Unit import Unit


class Engine(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\engine1.png'), pygame.image.load('data\\engine2.png'),
                                      pygame.image.load('data\\engine_not_working.png'),
                                      pygame.image.load('data\\engine_broken.png')], 'energy', 2, None)
        self.acceleration = 3
        self.health = 10

    def do(self):
        self.ship.distance += self.ship.velocity + self.acceleration