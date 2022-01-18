import  pygame

class A(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 2, 2)

class B(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(0, 1, 1, 1)

a = A()
b = B()

print(pygame.sprite.collide_rect(a, b))