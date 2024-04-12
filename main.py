# https://www.youtube.com/watch?v=txcOqDhrwBo&t=1962s
# ha olika typer av väggar som stutsväggar och klibbiga väggar


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

BG = pygame.image.load("img/bg.png")

player = [120, 500]
max_speed = 110
player_radius = 10

space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(WIN)

wall_color = (5, 102, 8)
wall_width = 125
wall_height = 10
wall_x = (WIDTH - wall_width) 
wall_y = (HEIGHT,  wall_height)

walls = [
    [(980, 0), (980, 600), (1000, 600), (1000, 0)],
    [(0, 0), (0, 600), (20, 600), (20, 0)],
    [(20, 0), (20, 20), (220, 20), (220, 0)],
    [(220, 0), (220, 600), (240, 600), (240, 0)],
    [(20, 580), (20, 600), (220, 600), (220, 580)],
    [(20, 200), (20, 210), (145, 210), (145, 200)],
    [(95, 350), (95, 360), (220, 360), (220, 350)]
]

def create_walls(poly_dims):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = ((0, 0))
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 0.8

    space.add(body, shape)

for c in walls:
    create_walls(c)

def create_ball(radius, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    shape.elasticity = 0.8
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

        WIN.blit(BG, (0, 0))
        pygame.draw.rect(WIN, wall_color, (95, 350, wall_width, wall_height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.body.apply_impulse_at_local_point((2000, 0), (0, 0)) 

        left_click = False
        
        mx, my = pygame.mouse.get_pos()

        direction_vector = [mx - player[0], my - player[1]]

        length = min(110, math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2))
        
        end_point = (player[0] + length * direction_vector[0] / (math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)),
                     player[1] + length * direction_vector[1] / (math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)))


        
        
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

        pygame.draw.circle(WIN, "black", [120, 80], player_radius)
        #pygame.draw.line(WIN, "black", (player), (end_point), 3)
        #pygame.draw.circle(WIN, "white", (player), player_radius)
        
        space.debug_draw(draw_options)
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()