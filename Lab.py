import  pygame

class Lab:
    def __init__(self, ship, x, y):
        self.images = [pygame.image.load('data\\lab1.png'), pygame.image.load('data\\lab1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.ship = ship
        self.working = True
        self.x = x
        self.y = y
        self.rect.move(self.x * self.ship.cell_size, self.y * self.ship.cell_size)
        self.ship.map[y][x] = 'l'
        for y in range(y + 1, y + 4):
            for x in range(x + 1, x + 3):
                self.ship.map[y][x] = 'o'
        self.ship.every_single_unit['labs'].append(self)

    def tick(self):
        self.ship.resourses['science'] += 3