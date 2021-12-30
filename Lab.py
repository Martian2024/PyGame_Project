import  pygame

class Lab(pygame.sprite.Sprite):
    def __init__(self, ship, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 10
        self.ship = ship
        self.images = [pygame.image.load('data\\lab1.png'), pygame.image.load('data\\lab2.png')]
        self.image = self.images[0]
        self.image_not_working = pygame.image.load('data\\lab_not_working.png')
        self.image_broken = pygame.image.load('data\\lab_broken.png')
        self.rect = pygame.Rect(x * self.ship.cell_size, y * self.ship.cell_size, 90, 90)
        self.counter = 1
        self.consume = 3
        self.working = True
        self.broken = False
        self.x = x
        self.y = y
        self.ship.map[y][x] = self
        for y in range(y + 1, y + 4):
            for x in range(x + 1, x + 3):
                self.ship.map[y][x] = self
        self.ship.every_single_unit['labs'].append(self)

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