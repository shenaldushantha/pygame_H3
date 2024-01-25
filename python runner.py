import sys
import pygame
from pygame.locals import *

pygame.init()

width = 1000
height = 600
dispSurf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner 1.0")

level = pygame.image.load("bak.jpeg").convert()
mario = pygame.image.load("runner.jpeg").convert()
fireball = pygame.image.load("hm.jpeg").convert()
rectangle = pygame.Surface((600, 15))
rectangle.fill((0, 0, 255))

fireballArea = fireball.get_rect()
marioArea = mario.get_rect()
rectangleArea = rectangle.get_rect()

marioArea.left = 400
marioArea.top = 500
rectangleArea.left = 0
rectangleArea.top = 200

speed = [1, 1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    fireballArea.move_ip(speed)

    if fireballArea.left < 0 or fireballArea.right > width:
        speed[0] = -speed[0]
    if fireballArea.top < 0 or fireballArea.bottom > height:
        speed[1] = -speed[1]

    if rectangleArea.colliderect(fireballArea):
        if rectangleArea.colliderect(fireballArea.move(-speed[0], 0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]

    pressings = pygame.key.get_pressed()
    if pressings[K_LEFT]:
        marioArea.move_ip((-1, 0))
    if pressings[K_RIGHT]:
        marioArea.move_ip((1, 0))
    if pressings[K_DOWN]:
        marioArea.move_ip((0, 1))
    if pressings[K_UP]:
        marioArea.move_ip((0, -1))

    dispSurf.fill((0, 0, 0))  # Clear the screen before redrawing

    dispSurf.blit(level, (0, 0))
    dispSurf.blit(fireball, fireballArea)
    dispSurf.blit(mario, marioArea)
    dispSurf.blit(rectangle, rectangleArea)

    pygame.display.flip()