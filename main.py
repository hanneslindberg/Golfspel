import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

BG = pygame.image.load("bg.png")

player = [WIDTH/2, HEIGHT/2]

PLAYER_RADIUS = 10

timer = pygame.time.Clock   



def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        WIN.blit(BG, (0, 0))

        mx, my = pygame.mouse.get_pos()

        dx = mx - player[0]
        dy = my - player[1]
        
        length = min(100, (dx ** 2 + dy ** 2) ** 0.5)
        
        end_point = (player[0] + length * dx / ((dx ** 2 + dy ** 2) ** 0.5), player[1] + length * dy / ((dx ** 2 + dy ** 2) ** 0.5))

        pygame.draw.line(WIN, "black", (player), (end_point), 3)
        pygame.draw.circle(WIN, "white", (player), PLAYER_RADIUS)
    
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
