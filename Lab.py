import  pygame
from Unit import Unit

class Lab(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y,
                         [pygame.image.load('data\\lab1.png'), pygame.image.load('data\\lab2.png'),
                          pygame.image.load('data\\lab_not_working.png'), pygame.image.load('data\\lab_broken.png')],
                         'science', 3, ['energy'])
        self.health = 10
        self.max_health = 10

    def do(self):
        if self.working:
            if self.ship.resourses['energy'] >= 3:
                self.ship.resourses['science'] += 3
                self.ship.resourses['energy'] -= 3
            else:
                self.working = False
        self.new_image()