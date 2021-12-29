import pygame

class PowerPlant(pygame.sprite.Sprite):
    def __init__(self, ship, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.ship = ship
        self.x = x
        self.y = y
        self.broken = False
        self.working = True
        self.counter = 1
        self.counter_of_consume = 1
        self.image_index = 0
        self.images = [pygame.image.load('data\\powerplant1.png'), pygame.image.load('data\\powerplant2.png')]
        self.image_broken = pygame.image.load('data\\powerplant_broken.png')
        self.image_not_working = pygame.image.load('data\\powerplant_not_working.png')
        self.image = self.images[self.image_index]
        self.rect = pygame.Rect(x * self.ship.cell_size, y * self.ship.cell_size, 90, 90)
        self.ship.map[y][x] = self
        for y in range(y + 1, y + 2):
            for x in range(x + 1, x + 2):
                self.ship.map[y][x] = self
        self.ship.every_single_unit['energy'].append(self)

    def new_image(self):
        if self.broken:
            self.image = self.image_broken
            self.counter = 1
        elif not self.working:
            self.image = self.image_not_working
            self.counter = 1
        else:
            if self.counter == 30:
                self.counter = 1
                self.image = self.images[self.images.index(self.image) - 1]
            else:
                self.counter += 1

    def do(self):
        if self.working:
            self.ship.resourses['energy'] += 3