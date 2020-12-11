import pygame

from VisibleObject import *
from sprites import *

class Dinosaur(VisibleObject):
    POSITION = Vector2(80, 300)
    POSITION_DUCKING = Vector2(80, 134)
    
    def __init__(self, ground):
        # Call Update method from base class
        super().__init__(DINO_RUNNING[0])
        
        self.position.x = self.POSITION.x
        self.position.y = self.POSITION.y

        self.isRunning = True
        self.isDucking = False
        self.isJumping = False

        self.speed = 1
        self.acceleration = Vector2(0, 0)
        self.friction = -0.02

        self.gravitation = 2

        self.step_index = 0

        self.ground = ground

    def update(self):
        self.step_index %= 10

        self.acceleration = Vector2(0, self.gravitation)

        keys = pygame.key.get_pressed()
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if (keys[pygame.K_s] and not self.isJumping):
            self.Duck()
            self.position.y = self.position.y + 34
            self.isDucking = True
            self.isRunning = False
        else:
            self.Run()
            self.isDucking = False
            self.isRunning = True

        self.rect.midbottom = self.position

        if self.velocity.y > 0:
            hit = self.rect.colliderect(self.ground.rect)
            if (hit):
                self.position.y = self.ground.rect.top
                self.velocity.y = 0
                self.isJumping = False
            else:
                self.isJumping = True

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def Run(self):
        self.image = DINO_RUNNING[self.step_index // 5]
        self.step_index += 1
    
    def Duck(self):
        self.image = DINO_DUCKING[self.step_index // 5]
        self.step_index += 1

    def Jump(self):
        self.rect.x += 1
        hit = self.rect.colliderect(self.ground.rect)
        self.rect.x -= 1
        if hit:
            self.isJumping = True
            self.velocity.y = -30