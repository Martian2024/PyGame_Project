import pygame
from Unit import Unit

class PowerPlant(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y,
                         [pygame.image.load('data\\powerplant1.png'), pygame.image.load('data\\powerplant2.png'),
                          pygame.image.load('data\\powerplant_not_working.png'),
                          pygame.image.load('data\\powerplant_broken.png')], 'energy', 3, None)

    def new_image(self):
        if self.broken:
            self.image = self.image_broken
            self.counter = 1
        elif not self.working:
            self.image = self.image_not_working
            self.counter = 1
        else:
            if self.counter == 30:
                self.image = self.images[self.images.index(self.image) - 1]
                self.counter += 1
            elif self.counter == 60:
                self.image = self.images[self.images.index(self.image) - 1]
                self.counter = 1
            elif self.counter == 1:
                self.image = self.images[0]
                self.counter += 1
            else:
                self.counter += 1

    def output(self):
        if self.working:
            self.ship.resourses['energy'] += 3