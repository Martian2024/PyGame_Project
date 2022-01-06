import pygame
from Unit import Unit

class PowerPlant(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y,
                         [pygame.image.load('data\\powerplant1.png'), pygame.image.load('data\\powerplant2.png'),
                          pygame.image.load('data\\powerplant_not_working.png'),
                          pygame.image.load('data\\powerplant_broken.png')], 'energy', 20, None)
        self.health = 10
        self.max_health = 10

    def output(self):
        if self.working:
            self.ship.resourses['energy'] += 3