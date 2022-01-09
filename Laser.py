import pygame
from Unit import Unit

class Laser(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\Laser1.png'),
                                      pygame.image.load('data\\Laser2.png'),
                                      pygame.image.load('data\\Laser_not_working.png'),
                                      pygame.image.load('data\\Laser_broken.png')], 'armor', 10, ['energy'])
        self.cooldown = 0
        self.ship.cannons.append(self)


    def do(self):
        if self.health < self.max_health // 2:
            self.broken = True
            self.working = False
        self.new_image()


    def shoot(self, ast):
        if self.working:
            if self.cooldown == 0:
                pygame.draw.line(self.ship.screen, (0, 211, 255), self.rect.center, ast.rect.center, 5)
                ast.kill()
            if 0 < self.cooldown < 100:
                self.cooldown += 1
            else:
                self.cooldown = 0