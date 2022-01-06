import pygame
import sys

pygame.font.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect =  image.get_rect()
        self.status = False
        self.rect.move_ip(x, y)

class Menu_Button(Button):
    def __init__(self, x, y, image, ship):
        super().__init__(x, y, image)
        self.ship = ship
        self.text = pygame.font.Font(None, 12)

    def pressed(self, screen):
        screen.fill(pygame.Color('white'))
        for cat in self.ship.resourses.keys():
            screen.blit(self.text.render('{}: {}'.format(cat, str(self.ship.resourses[cat]))),
                        False, pygame.Color('white'), (0, 0))
        screen.update()
        while self.status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                       if self.rect.collidepoint(event.pos):
                           self.status = False
