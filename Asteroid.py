import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load('data\\asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.speed = -5
        self.speed_angle = random.randint(-15, 15)
        self.angle = 0

    def move(self):
        self.angle += self.speed_angle
        self.image = pygame.transform.rotate(pygame.image.load('data\\asteroid.png'), self.angle)
        self.x += self.speed
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)