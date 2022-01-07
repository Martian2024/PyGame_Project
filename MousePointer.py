import pygame

class MousePointer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.prev_x = 0
        self.prev_y = 0
        self.im = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.rect = self.im.get_rect()

    def move(self, x, y):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x
        self.y = y
        self.rect.move_ip(x - self.prev_x, y - self.prev_y)