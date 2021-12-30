import pygame

class Farm(pygame.sprite.Sprite):
    def __init__(self, ship, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 10
        self.ship = ship
        self.consume = 3
        self.x = x
        self.y = y
        self.image_working = pygame.image.load('data\\farm.png')
        self.image_broken = pygame.image.load('data\\farm_broken.png')
        self.image_not_working = pygame.image.load('data\\farm_not_working.png')
        self.image = self.image_working
        self.working = True
        self.broken = False
        self.ship.map[y][x] = self
        for y in range(y + 1, y + 4):
            for x in range(x + 1, x + 3):
                self.ship.map[y][x] = self
        self.ship.every_single_unit['farms'].append(self)
        self.rect = pygame.Rect(x * self.ship.cell_size, y * self.ship.cell_size, 150, 90)

    def do(self):
        if self.working:
            self.ship.resourses['food'] += 3
        self.new_image()

    def new_image(self):
        if self.broken:
            self.image = self.image_broken
        elif not self.working:
            self.image = self.image_not_working
        else:
            self.image = self.image_working