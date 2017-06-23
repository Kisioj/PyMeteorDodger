import sys, pygame
from pygame.locals import *
import random

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

meteor_images = [
    pygame.image.load("meteor1.png"),
    pygame.image.load("meteor2.png"),
    pygame.image.load("meteor3.png"),
    pygame.image.load("meteor4.png"),
    pygame.image.load("meteor5.png"),
    pygame.image.load("meteor6.png"),
    pygame.image.load("meteor7.png"),
    pygame.image.load("meteor8.png")
]
meteors = []
        
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
    
    if random.randint(1, 30) == 1:
        meteor_image = random.choice(meteor_images)
        meteor = GameObject(meteor_image)
        meteor.rect.x = random.randint(-50, 462)
        meteor.rect.y = -meteor.rect.h
        meteors.append(meteor)
    
    background_rect.y += 4
    if background_rect.y >= 0:
        background_rect.y -= 768
 
    screen.blit(background_image, background_rect)
    spaceship.render()
    for meteor in meteors:
        meteor.rect.y += 8
        meteor.render()
    meteors = [meteor for meteor in meteors if meteor.rect.y < height]
    
    pygame.display.flip()
    clock.tick(60)
