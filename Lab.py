import  pygame

class Lab:
    def __init__(self, ship, x, y):
        self.health = 10
        self.images = [pygame.image.load('data\\lab1.png'), pygame.image.load('data\\lab2.png')]
        self.image = self.images[0]
        self.image_not_working = pygame.image.load('data\\lab_not_working.png')
        self.image_broken = pygame.image.load('data\\lab_broken.png')
        self.counter = 1
        self.consume = 3
        self.rect = self.image.get_rect()
        self.ship = ship
        self.working = True
        self.broken = False
        self.x = x
        self.y = y
        self.ship.map[y][x] = 'l'
        for y in range(y + 1, y + 4):
            for x in range(x + 1, x + 3):
                self.ship.map[y][x] = 'o'
        self.ship.every_single_unit['labs'].append(self)

    def tick(self):
        if self.working:
            self.ship.resourses['science'] += 3

    def new_image(self):
        if self.broken:
            self.image = self.image_broken
        elif not self.working:
            self.image = self.image_not_working
        else:
            if self.counter == 30:
                self.image = self.images[self.images.index(self.image) - 1]
                self.counter = 1
            else:
                self.counter += 1