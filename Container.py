import pygame
import random
class Container(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image= pygame.image.load('data\\container.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = random.randint(-8, -1)
        self.angle = 0
        self.speed_angle = random.randint(-8, 8)

    def move(self):
        self.angle += self.speed_angle
        self.x += self.speed
        self.image = pygame.transform.rotate(pygame.image.load('data\\container.png'), self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)