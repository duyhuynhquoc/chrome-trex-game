import pygame

Vector2 = pygame.math.Vector2

class VisibleObject(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 0
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.friction = 0

        self.gravitation = 0

        self.position = Vector2(0, 0)

    def update(self):
        pass

