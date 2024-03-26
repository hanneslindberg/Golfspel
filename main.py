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
max_speed = 110
player_radius = 10
 
left_click = False

def main():
    run = True

    while run:
        left_click = False

        mx, my = pygame.mouse.get_pos()

        direction_vector = [mx - player[0], my - player[1]]

        length = min(110, math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2))
        
        end_point = (player[0] + length * direction_vector[0] / (math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)),
                     player[1] + length * direction_vector[1] / (math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_click = True

        WIN.blit(BG, (0, 0))

        
        if left_click == True:
            if length != 0:
                direction_vector[0] /= length
                direction_vector[1] /= length
            
            speed = max_speed * (length / 100)

            new_ball_pos = [player[0] + direction_vector[0] * speed, player[1] + direction_vector[1] * speed]

            player[0] = new_ball_pos[0]
            player[1] = new_ball_pos[1]

        pygame.draw.circle(WIN, "black", [800, 100], player_radius)
        pygame.draw.line(WIN, "black", (player), (end_point), 3)
        pygame.draw.circle(WIN, "white", (player), player_radius)
        
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()



    #Crashar för att man inte kan dividera med "0"