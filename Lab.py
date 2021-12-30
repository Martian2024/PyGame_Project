import  pygame
from Unit import Unit

class Lab(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y,
                         [pygame.image.load('data\\lab1.png'), pygame.image.load('data\\lab2.png'),
                          pygame.image.load('data\\lab_not_working.png'), pygame.image.load('data\\lab_broken.png')],
                         'science', 3, 'energy')

    def do(self):
        if self.working:
            if self.ship.resourses['energy'] >= 3:
                self.ship.resourses['science'] += 3
                self.ship.resourses['energy'] -= 3
            else:
                self.working = False
        self.new_image()

    def new_image(self):
        if self.broken:
            self.image = self.image_broken
            self.counter = 1
        elif not self.working:
            self.image = self.image_not_working
            self.counter = 1
        else:
            if self.counter == 30:
                self.image = self.images[self.images.index(self.image) - 1]
                self.counter += 1
            elif self.counter == 60:
                self.image = self.images[self.images.index(self.image) - 1]
                self.counter = 1
            elif self.counter == 1:
                self.image = self.images[0]
                self.counter += 1
            else:
                self.counter += 1