import pygame
import time
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Golfspel")

BG = pygame.image.load("bg.png")

player = [WIDTH/2, HEIGHT/2]
max_speed = 36.2
player_radius = 10
 
left_click = False

def main():
    run = True

    while run:
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_click = True

        WIN.blit(BG, (0, 0))

        mx, my = pygame.mouse.get_pos()

        direction_vector = [mx - player[0], my - player[1]]

        length = min(100, math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2))
        
        if left_click == True:
            if length != 0:
                direction_vector[0] /= length
                direction_vector[1] /= length
            
            speed = max_speed * (length / 100)

            new_ball_pos = [player[0] + direction_vector[0] * speed, player[1] + direction_vector[1] * speed]

            alpha = 0.1
            player[0] = (1 - alpha) * player[0] + alpha * new_ball_pos[0]
            player[1] = (1 - alpha) * player[1] + alpha * new_ball_pos[1]

        end_point = (player[0] + length * direction_vector[0], player[1] + length * direction_vector[1])

        pygame.draw.line(WIN, "black", (int(player[0]), int(player[1])), (int(end_point[0]), int(end_point[1])), 3)
        pygame.draw.circle(WIN, "white", (int(player[0]), int(player[1])), player_radius)
    
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()
