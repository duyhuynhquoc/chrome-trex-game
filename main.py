import pygame

from config import *
from colors import *
from Dinosaur import *
from Ground import *

pygame.init()

SCREEN = pygame.display.set_mode(WINDOW_SIZE)

ground = Ground()
dino = Dinosaur(ground)
sprites = pygame.sprite.Group()
sprites.add(dino)
sprites.add(ground)

def main():
    gameExit = False
    clock = pygame.time.Clock()

    while not gameExit:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dino.Jump()

        SCREEN.fill(WHITE)
        sprites.draw(SCREEN)
        pygame.display.flip()

        sprites.update()

main() 