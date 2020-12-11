import pygame

from config import *
from colors import *
from Dinosaur import *
from Ground import *
from Cloud import *
from Background import *

pygame.init()

SCREEN = pygame.display.set_mode(WINDOW_SIZE)


global gameSpeed
gameSpeed = 15

global score
score = 0

ground = Ground()
cloud1 = Cloud(gameSpeed, 1)
cloud2 = Cloud(gameSpeed, 1.1)
dino = Dinosaur(ground)
background1 = Background(gameSpeed)
background2 = Background(gameSpeed)

sprites = pygame.sprite.Group()
sprites.add(dino)
sprites.add(ground)
sprites.add(cloud1)
sprites.add(background1)
sprites.add(background2)
#sprites.add(cloud2)

global curBG, nextBG
curBG = 0
nextBG = 1

font = pygame.font.Font('freesansbold.ttf', 20)

def Background():
    global curBG, nextBG
    bg = [background1, background2]
    if (bg[curBG].rect.right < WINDOW_SIZE[0]):
        bg[nextBG].rect.left = bg[curBG].rect.right
    if (bg[curBG].rect.right < 0):
        temp = curBG
        curBG = nextBG
        nextBG = temp

def Score():
    global score, gameSpeed
    score += 1
    if (score % 100 == 0):
        gameSpeed += 1

    text = font.render("Points: " + str(score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    SCREEN.blit(text, textRect)

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
        sprites.update()

        Background()

        Score()

        pygame.display.flip()

main() 