import pygame

class Farm(pygame.sprite.Sprite):
    def __init__(self, ship, x, y):
        self.health = 10
        self.ship = ship
        self.consume = 3
        self.x = x
        self.y = y
        self.image_working = pygame.image.load('data\\farm.png')
        self.image_not_working = pygame.image.load('data\\farm_broken.png')
        self.image = self.image_working
        self.working = True
        self.ship.map[y][x] = 'f'
        for y in range(y + 1, y + 4):
            for x in range(x + 1, x + 3):
                self.ship.map[y][x] = 'o'
        self.ship.every_single_unit['farms'].append(self)

    def tick(self):
        if self.working:
            if self.ship.resourses['H2O'] != 0 and self.ship.resourses['CO2'] != 0:
                self.ship.resourses['H2O'] -= self.consume
                self.ship.resourses['CO2'] -= self.consume

    def new_image(self):
        if not self.working:
            self.image = self.image_not_working
        else:
            self.image = self.image_working