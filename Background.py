import pygame
import random

from config import *
from VisibleObject import *
from sprites import *

class Background(VisibleObject):
    def __init__(self, gameSpeed):
        super().__init__(BACKGROUND)
        self.gameSpeed = gameSpeed
        self.rect.x = 0
        self.rect.y = 480
        
        
    def update(self):
        self.rect.x -= self.gameSpeed
