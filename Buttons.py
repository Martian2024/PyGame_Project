import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect =  image.get_rect()
        self.status = False
        self.rect.move_ip(x, y)

class Menu_Button(Button):
    def pressed(self):
        pass
