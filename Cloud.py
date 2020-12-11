import pygame
import random

from config import *
from VisibleObject import *
from sprites import *

class Cloud(VisibleObject):
    def __init__(self, gameSpeed, coefficient):
        super().__init__(CLOUD)
        self.gameSpeed = gameSpeed
        self.coefficient = coefficient

        self.rect.x = WINDOW_SIZE[0] + random.randint(200, 1000) * self.coefficient
        self.rect.y = random.randint(20, 50) * self.coefficient
        
        
    def update(self):
        self.rect.x -= self.gameSpeed

        if (self.rect.right < 0):
            self.rect.x = WINDOW_SIZE[0] + self.image.get_width()
            self.rect.y = random.randint(50, 200) * self.coefficient
