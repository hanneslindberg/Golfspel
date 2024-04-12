# https://www.youtube.com/watch?v=txcOqDhrwBo&t=1962s
# Lägga in bilder på pymunk object 38:00
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
club_image = pygame.image.load("img/club.png").convert_alpha()

pos = [120, 500]
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


ball = create_ball(player_radius, pos)

class Club:
    def __init__(self, pos):
        self.original_image = club_image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, angle):
        self.angle = angle

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, self.rect)

club = Club(ball.body.position)

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

        mouse_pos = pygame.mouse.get_pos()
        x_dist = ball.body.position[0] - mouse_pos[0]
        y_dist = -(ball.body.position[1] - mouse_pos[1])
        club_angle = math.degrees(math.atan2(y_dist, x_dist))
        club.update(club_angle)
        club.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.body.apply_impulse_at_local_point((2000, 0), (0, 0)) 

        #left_click = False

        #direction_vector = [mx - pos[0], my - pos[1]]

        #length = min(110, math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2))
        
        #end_point = (pos[0] + length * direction_vector[0] / (math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)),
                     #pos[1] + length * direction_vector[1] / (math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)))


        
        
        #if left_click == True:
            #if length != 0:
                #direction_vector[0] /= length
                #direction_vector[1] /= length
            
            #speed = max_speed * (length / 100)

            #new_ball_pos = [pos[0] + direction_vector[0] * speed, pos[1] + direction_vector[1] * speed]

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





           # pos[0] = new_ball_pos[0]
            #pos[1] = new_ball_pos[1]

        pygame.draw.circle(WIN, "black", [120, 80], player_radius)
        #pygame.draw.line(WIN, "black", (pos), (end_point), 3)
        #pygame.draw.circle(WIN, "white", (pos), player_radius)
        
        space.debug_draw(draw_options)
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()