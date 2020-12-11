import pygame

from VisibleObject import *
from sprites import *
from config import *
from Obstacle import *

class Bird(Obstacle):
    def __init__(self, image, gameSpeed):
        self.type = 0
        super().__init__(image, self.type, gameSpeed)
        self.rect.y = 330
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1