import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, current_dif):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if random.randint(1, 3) == 1:
            self.image = pygame.image.load('data\\bigger_asteroid.png')
            self.size = 'big'
        else:
            self.size = 'small'
            self.image = pygame.image.load('data\\asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.speed = random.randint(int(-4 + (-1 / current_dif)), -2)
        self.speed_angle = random.randint(-15, 15)
        self.angle = 0

    def move(self):
        self.angle += self.speed_angle
        if self.size == 'big':
            self.image = pygame.transform.rotate(pygame.image.load('data\\bigger_asteroid.png'), self.angle)
        else:
            self.image = pygame.transform.rotate(pygame.image.load('data\\asteroid.png'), self.angle)
        self.x += self.speed
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)