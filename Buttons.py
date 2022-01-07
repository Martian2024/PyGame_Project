import pygame
import sys

pygame.font.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.rect =  image.get_rect()
        self.status = False

class Menu_Button(Button):
    def __init__(self, x, y, image, ship):
        super().__init__(x, y, image)
        self.ship = ship
        self.text = pygame.font.Font(None, 12)

    def pressed(self, pause, abnormal_blit):
        if abnormal_blit == 'Telemetry':
            abnormal_blit = 'None'
        else:
            abnormal_blit = 'Telemetry'
        if pause:
            pause = False
        else:
            pause = True
        while self.status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                       if self.rect.collidepoint(event.pos):
                           self.status = False
        return pause, abnormal_blit