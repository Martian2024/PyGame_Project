import pygame

class Armor(pygame.sprite.Sprite):
    def __init__(self, ship, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 10
        self.x = x
        self.y = y
        self.ship = ship
        self.image_ok = pygame.image.load('data\\armor_ok.png')
        self.image_damaged = pygame.image.load('data\\armor_damaged.png')
        self.image = self.image_ok
        self.damaged = False
        self.ship.map[y][x] = self
        self.ship.every_single_unit['armor'].append(self)
        self.rect = pygame.Rect(x * self.ship.cell_size, y * self.ship.cell_size, 30, 30)

    def new_image(self):
        if self.damaged == True:
            self.image = self.image_damaged
        else:
            self.image = self.image_ok

    def do(self):
        pass