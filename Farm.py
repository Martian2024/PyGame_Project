import pygame
from Unit import Unit

class Farm(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\farm.png'), pygame.image.load('data\\farm_not_working.png'),
                                      pygame.image.load('data\\farm_broken.png')], 'food', 3, ['energy'])


    def new_image(self):
        if self.broken:
            self.image = self.image_broken
        elif not self.working:
            self.image = self.image_not_working
        else:
            self.image = self.image_working