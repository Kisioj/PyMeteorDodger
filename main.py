import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 512, 768
pygame.display.set_caption("Asteroid Dodger")
screen = pygame.display.set_mode(size)

background_image = pygame.image.load("background.png").convert()
background_rect = background_image.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.blit(background_image, background_rect)
    pygame.display.flip()
