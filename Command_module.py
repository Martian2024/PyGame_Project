import pygame
from Unit import Unit

class Comand_Module(Unit):
    def __init__(self, ship, x, y):
        super().__init__(ship, x, y, [pygame.image.load('data\\command_module1.png'),
                                      pygame.image.load('data\\command_module2.png'),
                                      pygame.image.load('data\\command_module_not_working.png'),
                                      pygame.image.load('data\\command_module_broken.png')], 'commands', 5, ['energy'])
        self.ship.controls.append(self)

    def do(self):
        flag = True
        for i in self.consume_cat:
            if self.ship.resourses[i] < self.consume:
                flag = False
        if not flag:
            self.working = False
        self.new_image()