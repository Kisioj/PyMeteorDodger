import sys, pygame
from pygame.locals import *
import random

class GameObject:
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()
        self.angle = 0
        
    def render(self):
        if self.angle > 0:
            image, rect = self.rotated_image()
        else:
            image, rect = self.image, self.rect
    
        screen.blit(image, rect)

    def rotated_image(self):
        image = pygame.transform.rotate(self.image, self.angle)
        rect = image.get_rect()
        rect.center = self.rect.center
        return image, rect
        
    def small_rect(self):
        return Rect(self.rect.x + 15, self.rect.y + 30, 69, 5)
        
pygame.init()
pygame.font.init()
font = pygame.font.Font("star.ttf", 30)
white = (255, 255, 255)
game_over_text = font.render("game over", True, white)

size = width, height = 512, 768
pygame.display.set_caption("Asteroid Dodger")
screen = pygame.display.set_mode(size)
keys_down = set()
clock = pygame.time.Clock()
game_over = False
points = 0

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

bonus_images = [
    pygame.image.load("pill_blue.png"),
    pygame.image.load("pill_green.png"),
    pygame.image.load("pill_red.png"),
    pygame.image.load("pill_yellow.png")
]
bonuses = []
        
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            keys_down.add(event.key)
        if event.type == KEYUP:
            keys_down.remove(event.key)
    
    if not game_over:
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
        elif random.randint(1, 100) == 1:
            bonus_image = random.choice(bonus_images)
            bonus = GameObject(bonus_image)
            bonus.rect.x = random.randint(0, 490)
            bonus.rect.y = -bonus.rect.h
            bonuses.append(bonus)
        
        background_rect.y += 4
        if background_rect.y >= 0:
            background_rect.y -= 768
     
        screen.blit(background_image, background_rect)
        spaceship.render()
        for bonus in bonuses:
            bonus.rect.y += 4
            bonus.angle -= 4
            bonus.angle %= 360
            bonus.render()
            if spaceship.rect.colliderect(bonus.rect):
                bonus.rect.y = height
                points += 1
                
        bonuses = [bonus for bonus in bonuses if bonus.rect.x < height]
            
        for meteor in meteors:
            meteor.rect.y += 8
            meteor.angle += 1
            meteor.angle %= 360
            meteor.render()
            if spaceship.small_rect().colliderect(meteor.rect):
                game_over = True

                
        meteors = [meteor for meteor in meteors if meteor.rect.y < height]
        
        if game_over:
            screen.blit(game_over_text, (width / 2 - game_over_text.get_rect().w / 2, height / 2 - 100))
            pygame.draw.rect(screen, white, spaceship.small_rect())
        
        points_text = font.render("pills: " + str(points), True, white)
        screen.blit(points_text, (10, 0))
        
        pygame.display.flip()
    clock.tick(60)
