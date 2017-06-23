import sys, pygame
from pygame.locals import *

class GameObject:
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()
        
    def render(self):
        screen.blit(self.image, self.rect)

pygame.init()
size = width, height = 512, 768
pygame.display.set_caption("Asteroid Dodger")
screen = pygame.display.set_mode(size)
keys_down = set()
clock = pygame.time.Clock()

background_image = pygame.image.load("background.png").convert()
background_rect = background_image.get_rect()

spaceship_image = pygame.image.load("spaceship.png")
spaceship = GameObject(spaceship_image)
spaceship.rect.y = height - spaceship.rect.h

        
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            keys_down.add(event.key)
        if event.type == KEYUP:
            keys_down.remove(event.key)
            
    if K_LEFT in keys_down and spaceship.rect.x > 0:
        spaceship.rect.x -= 8
    if K_RIGHT in keys_down and spaceship.rect.x + spaceship.rect.w < width:
        spaceship.rect.x += 8
    
    background_rect.y += 4
    if background_rect.y >= 0:
        background_rect.y -= 768

    screen.blit(background_image, background_rect)
    spaceship.render()
    pygame.display.flip()
    clock.tick(60)
