import pygame
import random

from VisibleObject import *
from sprites import *
from config import *

class Obstacle(VisibleObject):
    def __init__(self, image, type, gameSpeed):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = WINDOW_SIZE[0]
        self.gameSpeed = gameSpeed

    def update(self):
        
        self.rect.x -= self.gameSpeed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)