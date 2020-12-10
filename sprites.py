import pygame
import os

# DINO SPRITES
DINO_RUNNING = [
    pygame.image.load(os.path.join('Assets/Dino', 'DinoRun1.png')),
    pygame.image.load(os.path.join('Assets/Dino', 'DinoRun2.png'))
]

DINO_JUMPING = pygame.image.load(os.path.join('Assets/Dino', 'DinoJump.png'))

DINO_DUCKING = [
    pygame.image.load(os.path.join('Assets/Dino', 'DinoDuck1.png')),
    pygame.image.load(os.path.join('Assets/Dino', 'DinoDuck2.png'))
]

# CACTUS SPRITES
CACTUS_SMALL = [
    pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus1.png')),
    pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus2.png')),
    pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus3.png'))
]

CACTUS_LARGE = [
    pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus1.png')),
    pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus2.png')),
    pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus3.png'))
]

# BIRD SPRITES
BIRD = [
    pygame.image.load(os.path.join('Assets/Bird', 'Bird1.png')),
    pygame.image.load(os.path.join('Assets/Bird', 'Bird2.png'))
]

# CLOUD SPRITE
CLOUD = pygame.image.load(os.path.join('Assets/Other', 'Cloud.png'))

# BACKGROUND SPRTIE
BG = pygame.image.load(os.path.join('Assets/Other', 'Track.png'))