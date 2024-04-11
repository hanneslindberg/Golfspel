import pygame
import pymunk
import pymunk.pygame_util
import time
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

BG = pygame.image.load("bg.png")

player = [100, 300]
max_speed = 110
player_radius = 15

space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(WIN)

def create_ball(radius, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0
    pivot.max_force = 1000


    space.add(body, shape, pivot)
    return shape

ball = create_ball(player_radius, player)

clock = pygame.time.Clock()
FPS = 60

left_click = False

def main():
    run = True

    while run:
        clock.tick(FPS)
        space.step(1 / FPS)

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
                ball.body.apply_impulse_at_local_point((1000, 0), (0, 0)) 

        WIN.blit(BG, (0, 0))

        
        if left_click == True:
            if length != 0:
                direction_vector[0] /= length
                direction_vector[1] /= length
            
            speed = max_speed * (length / 100)

            new_ball_pos = [player[0] + direction_vector[0] * speed, player[1] + direction_vector[1] * speed]

            # i = 0
            # while i <= 100:
            #     currentPlayerValue = player
            #     print("Jag är här")
            #     if player[0] <= new_ball_pos[0]:
            #         player[0] = 0.1*currentPlayerValue[0]
            #         # pygame.draw.circle(WIN, "white", (player), player_radius)
            #     elif player[0] >= new_ball_pos[0]:
            #         player[0] = 1.1*currentPlayerValue[0]
            #         # pygame.draw.circle(WIN, "white", (player), player_radius)
            #     if player[1] <= new_ball_pos[1]:q
            #         player[1] = 0.1*currentPlayerValue[1]
            #         # pygame.draw.circle(WIN, "white", (player), player_radius)
            #     elif player[1] >= new_ball_pos[1]:
            #         player[1] = 1.1*currentPlayerValue[1]    
                    # pygame.draw.circle(WIN, "white", (player), player_radius)
                
                # pygame.draw.circle(WIN, "white", (player), player_radius)





            player[0] = new_ball_pos[0]
            player[1] = new_ball_pos[1]

        pygame.draw.circle(WIN, "black", [800, 100], player_radius)
        #pygame.draw.line(WIN, "black", (player), (end_point), 3)
        #pygame.draw.circle(WIN, "white", (player), player_radius)
        
        space.debug_draw(draw_options)
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()