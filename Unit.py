import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, ship, x, y, images, cat, consume, consume_cat):
        pygame.sprite.Sprite.__init__(self)
        self.cat = cat
        self.consume = consume
        self.consume_cat = consume_cat
        self.x = x
        self.y = y
        self.ship = ship
        self.working = True
        self.broken = False
        self.counter = 0
        if len(images) == 3:
            self.images = images[:1]
            self.image = self.images[0]
            self.image_working = self.images[0]
            self.image_not_working = images[-2]
            self.image_broken = images[-1]
        else:
            self.images = images[:2]
            self.image = self.images[0]
            self.image_working = self.images[0]
            self.image_not_working = images[-2]
            self.image_broken = images[-1]
        self.rect = self.image.get_rect()
        self.rect.move_ip(x * ship.cell_size, y * ship.cell_size)
        self.ship.every_single_unit[self.cat].append(self)


    def new_image(self):
        if self.broken:
            self.image = self.image_broken
        elif not self.working:
            self.image = self.image_not_working
        else:
            if len(self.images) == 1:
                self.image = self.images[0]
            else:
                if self.counter == 60:
                    self.image = self.images[self.images.index(self.image) - 1]
                    self.counter = 1
                elif self.counter == 30:
                    self.image = self.images[self.images.index(self.image) - 1]
                    self.counter += 1
                elif self.counter == 1:
                    self.image = self.images[0]
                else:
                    self.counter += 1

    def do(self):
        if self.working:
            if self.consume_cat != None:
                flag = True
                for i in self.consume_cat:
                    if self.ship.resourses[i] < self.consume:
                        flag = False
                if flag:
                    self.ship.resourses[self.cat] += self.consume
                    for i in self.consume_cat:
                        self.ship.resourses[i] -= self.consume
                else:
                    self.working = False
            else:
                self.ship.resourses[self.cat] += self.consume