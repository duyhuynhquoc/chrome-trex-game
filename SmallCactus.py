import pygame
import random

from VisibleObject import *
from sprites import *
from config import *
from Obstacle import *

class SmallCactus(Obstacle):
    def __init__(self, image, gameSpeed):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type ,gameSpeed)
        self.rect.y = 425