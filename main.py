import sys, pygame

pygame.init()
size = width, height = 512, 768
pygame.display.set_caption("Asteroid Dodger")
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()