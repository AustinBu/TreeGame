import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))

window.fill((255, 255, 255))

pygame.draw.rect(window, (0, 0, 255),
                 [100, 100, 400, 100], 2)

pygame.display.update()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
