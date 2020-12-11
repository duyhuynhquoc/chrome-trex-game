import pygame

from VisibleObject import *
from colors import *

class Ground(VisibleObject):
    POSITION = Vector2(0, 500)

    def __init__(self):
        # Call Update method from base class
        image = pygame.Surface((1100, 100))
        image.fill(WHITE)
        super().__init__(image)
        
        self.rect.x = self.POSITION.x
        self.rect.y = self.POSITION.y

        self.isRunning = True
        self.isDucking = False
        self.isJumping = False

        self.speed = 1
        self.acceleration = Vector2(0, 0)
        self.friction = -0.02

        self.gravitation = 0

        self.step_index = 0

    def update(self):   
        # Call Update method from base class
        #super().update()
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))