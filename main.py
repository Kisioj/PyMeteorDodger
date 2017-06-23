import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 512, 768
pygame.display.set_caption("Asteroid Dodger")
screen = pygame.display.set_mode(size)
keys_down = set()
clock = pygame.time.Clock()


background_image = pygame.image.load("background.png").convert()
background_rect = background_image.get_rect()

spaceship_image = pygame.image.load("spaceship.png")
spaceship_rect = spaceship_image.get_rect()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            keys_down.add(event.key)
        if event.type == KEYUP:
            keys_down.remove(event.key)
            
    if K_LEFT in keys_down:
        spaceship_rect.x -= 8
    if K_RIGHT in keys_down:
        spaceship_rect.x += 8
            
    screen.blit(background_image, background_rect)
    screen.blit(spaceship_image, spaceship_rect)
    pygame.display.flip()
    clock.tick(60)
