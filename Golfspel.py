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

# Load images
ball_image = pygame.image.load("img/ball.png").convert_alpha()
club_image = pygame.image.load("img/club.png").convert_alpha()

clock = pygame.time.Clock()
FPS = 60

# Variables
PINK = (255, 105, 180)
DARK_GREEN = (14, 58, 0)
BUNKER = (255, 240, 152)

pos = [120, 500]
max_speed = 110
player_radius = 8
hole_rad = 10

taking_shot = True
powering_up = False
force = 0
max_force = 7000
force_direction = 1

i_wall_c = (255, 208, 79)
o_wall_c = (70, 51, 0)
wall_w = 125
wall_h = 10
shade = (0, 30, 0)


space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(WIN)

# Create starting points
starting_points = [
    (120, 500),
    (320, 525), 
    (520, 230)
]

# Create holes
holes = [
    (120, 80),
    (570, 80), 
    (900, 400)
]

# Create walls
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

# Create the ball
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

class Club():
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
        surface.blit(self.image, 
            (self.rect.centerx - self.image.get_width() / 2,
            self.rect.centery - self.image.get_height() / 2)        
        )

club = Club(ball.body.position)

power_bar = pygame.Surface((10, 20))
power_bar.fill("red")

run = True
while run:
    clock.tick(FPS)
    space.step(1 / FPS)

    # Draw background
    WIN.blit(BG, (0, 0))

    # Hill
    pygame.draw.circle(WIN, DARK_GREEN, (900, 400), 70)
    # Draw holes
    pygame.draw.circle(WIN, "black", (120, 80), hole_rad)
    pygame.draw.circle(WIN, "black", (570, 80), hole_rad)
    pygame.draw.circle(WIN, "black", (900, 400), hole_rad)
    
    # --- Inside wall shadow
    pygame.draw.rect(WIN, shade, (95, 350, wall_w + 2, wall_h + 2))
    pygame.draw.rect(WIN, shade, (21, 200, wall_w + 2, wall_h + 2))

    # --- Outside wall shadow
    pygame.draw.rect(WIN, shade, (0, 0, 1002, 22))
    pygame.draw.rect(WIN, shade, (0, 20, 22, 562))
    pygame.draw.rect(WIN, shade,  (220, 20, 22, 562))

    # Water
    pygame.draw.circle(WIN, BUNKER, (785, 160), 70)
    pygame.draw.circle(WIN, BUNKER, (850, 190), 50)

    # Inside walls
    pygame.draw.polygon(WIN, i_wall_c, ((241, 21), (320, 21), (241, 100)))
    pygame.draw.polygon(WIN, i_wall_c, ((290, 140), (400, 140), (400, 400)))
    pygame.draw.polygon(WIN, i_wall_c, ((241, 200), (241, 500), (330, 400)))

    pygame.draw.rect(WIN, i_wall_c, (95, 350, wall_w, wall_h))
    pygame.draw.rect(WIN, i_wall_c, (21, 200, wall_w, wall_h))

    # Outside walls
    pygame.draw.rect(WIN, o_wall_c, (0, 0, 1000, 20))
    pygame.draw.rect(WIN, o_wall_c, (0, 20, 20, 560))
    pygame.draw.rect(WIN, o_wall_c, (0, 580, 1000, 20))
    pygame.draw.rect(WIN, o_wall_c, (980, 20, 20, 560))
    pygame.draw.rect(WIN, o_wall_c, (220, 20, 20, 560))
    pygame.draw.rect(WIN, o_wall_c, (400, 140, 20, 560))
    pygame.draw.rect(WIN, o_wall_c, (420, 140, 200, 20))
    pygame.draw.rect(WIN, o_wall_c, (620, 20, 20, 400))
    pygame.draw.rect(WIN, o_wall_c, (800, 160, 20, 420))

    # Bouncy walls
    pygame.draw.rect(WIN, PINK, (410, 440, 15, 130))
    

    # Draw ball
    WIN.blit(ball_image, (ball.body.position - (player_radius, player_radius)))

    # Check if ball is in the hole
    for hole in holes:
        ball_x_dist = abs(ball.body.position[0] - hole[0])
        ball_y_dist = abs(ball.body.position[1] - hole[1])
        ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2))
        if ball_dist <= hole_rad:
            ball.body.velocity = (0, 0)
            if hole == holes[0]:
                ball.body.position = starting_points[1]
            if hole == holes[1]:
                ball.body.position = starting_points[2]
            if hole == holes[2]:
                ball.body.position = starting_points[0]

    # Adding velocity to the ball
    taking_shot = True
    if int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0:
        taking_shot = False

    # Shooting direction
    if taking_shot == True:
        mouse_pos = pygame.mouse.get_pos()
        club.rect.center = ball.body.position
        x_dist = ball.body.position[0] - mouse_pos[0]
        y_dist = -(ball.body.position[1] - mouse_pos[1])
        club_angle = math.degrees(math.atan2(y_dist, x_dist))
        club.update(club_angle)
        club.draw(WIN)

    # Poweing up while holding
    if powering_up == True:
        force += 200 * force_direction
        if force >= max_force or force <= 0:
            force_direction *= -1
        #draw power bars
        for b in range(math.ceil(force / 2000)):
            WIN.blit(power_bar, 
                (ball.body.position[0] - 30 + (b * 15), 
                (ball.body.position[1] + 30))
            )
    elif powering_up == False and taking_shot == True:
        x_impulse = math.cos(math.radians(club_angle))
        y_impulse = math.sin(math.radians(club_angle))
        ball.body.apply_impulse_at_local_point((force * -x_impulse, force * y_impulse), (0, 0)) 
        force = 0
        force_direction = 1

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and taking_shot == True:
            powering_up = True
        if event.type == pygame.MOUSEBUTTONUP and taking_shot == True:
            powering_up = False
        if event.type == pygame.QUIT:
            run = False

    #space.debug_draw(draw_options) # -------------------------------------------------göm denna när du är klar med att måla alla väggar!!!
    pygame.display.flip()
    
        
pygame.quit()

