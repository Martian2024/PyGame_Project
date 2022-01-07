import pygame
from Unit import Unit


class Engine(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\engine1.png'), pygame.image.load('data\\engine2.png'),
                                      pygame.image.load('data\\engine_not_working.png'),
                                      pygame.image.load('data\\engine_broken.png')], 'energy', 4, None)
        self.acceleration = 3
        self.health = 10

    def do(self):
        if self.working:
            self.ship.distance += self.ship.velocity + self.acceleration
            self.ship.resourses['energy'] += self.consume
        else:
            self.ship.distance += self.ship.velocity