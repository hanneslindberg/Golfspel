import pygame
import time
import random

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

BG = pygame.image.load("bg.png")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "white", player)
    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(player)    

    pygame.quit()

if __name__ == "__main__":
    main()
