# https://www.youtube.com/watch?v=txcOqDhrwBo&t=1962s

# ha olika typer av väggar som stutsväggar och klibbiga väggar

# Fråga Eirik hur man gör de groparna och kullarna

import pygame
import pymunk
import pymunk.pygame_util
import math

# Initiate pygaem
pygame.init()
BG = pygame.image.load("img/bg.png")
# Create window
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    clock.tick(FPS)

    # Draw background
    WIN.blit(BG, (0, 0))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    
pygame.quit()