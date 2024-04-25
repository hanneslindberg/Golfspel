# https://www.youtube.com/watch?v=txcOqDhrwBo&t=1962s

# Fråga Eirik hur man gör de groparna och kullarna

# Lägg till tid hur lång tid det tar för alla banor

# Lägg till main menu

import pygame
import pymunk
import pymunk.pygame_util
import math
import button
from pymunk.vec2d import Vec2d

# Initiate pygaem
pygame.init()
BG = pygame.image.load("img/bg.png")
# Create window
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

clock = pygame.time.Clock()
FPS = 60

# Load images
ball_image = pygame.image.load("img/ball.png").convert_alpha()
club_image = pygame.image.load("img/club.png").convert_alpha()
start_image = pygame.image.load("img/start_image.png").convert_alpha()
quit_image = pygame.image.load("img/quit_image.png").convert_alpha()

start_button = button.Button((WIDTH / 2) - 100, 150, start_image, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_image, 2)

space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(WIN)

# Variables
PINK = (255, 105, 180)
BUNKER = (255, 240, 152)
HILL = (119, 216, 87)
INNER_HILL = (161, 228, 134)

pos = [120, 500]
max_speed = 110
player_radius = 8
hole_rad = 10
pushSpeed = 0
pushSpeedAdd = 0.4
Vec2d(0, 0)

taking_shot = True
powering_up = False
force = 0
max_force = 7000
force_direction = 1
start_game = False

i_wall_c = (255, 208, 79)
o_wall_c = (70, 51, 0)
wall_w = 125
wall_h = 10
shade = (0, 30, 0)

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

# Wall dimentions
walls = [
    [(980, 0), (980, 600), (1000, 600), (1000, 0)],
    [(0, 0), (0, 600), (20, 600), (20, 0)],
    [(20, 0), (20, 20), (980, 20), (980, 0)],
    [(220, 0), (220, 600), (240, 600), (240, 0)],
    [(20, 580), (20, 600), (980, 600), (980, 580)],
    [(20, 200), (20, 210), (145, 210), (145, 200)],
    [(95, 350), (95, 360), (220, 360), (220, 350)],
    [(400, 140), (420, 140), (420, 580), (400, 580)],
    [(420, 140), (620, 140), (620, 160), (420, 160)],
    [(620, 20), (620, 420), (640, 420), (640, 20)],
    [(800, 160), (800, 580), (820, 580), (820, 160)],
    [(241, 21), (320, 21), (241, 100)],
    [(290, 140), (400, 140), (400, 400)],
    [(241, 200), (241, 500), (330, 400)],
    [(800, 400), (800, 580), (720, 580)],
]

bounce_walls = [
    [(410, 440), (410, 590), (425, 590), (425, 440)],
    [(425, 440), (425, 590), (480, 590)]
]

bunkers = [
    [795, 160, 50], 
    [835, 190, 30],
    [600, 635, 130],
    [900, 650, 130]
]

# Create walls
def create_walls(poly_dims):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = ((0, 0))
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 0.8

    space.add(body, shape)

for c in walls:
    create_walls(c)

# Create bounce walls
def create_bounce_walls(poly_dims):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = ((0, 0))
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 3

    space.add(body, shape)

for c in bounce_walls:
    create_bounce_walls(c)

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

power_bar = pygame.Surface((10, 15))
power_bar.fill("red")

run = True
while run:
    clock.tick(FPS)
    space.step(1 / FPS)
    
    if start_game == False:
        WIN.fill("black")
        taking_shot = False
        if start_button.draw(WIN):
            ball.body.position = pos
            ball.body.velocity = (0, 0)
            start_game = True 
        if quit_button.draw(WIN):
            run = False
    else:
        # Draw background
        WIN.blit(BG, (0, 0))
        # Hill
        # pygame.draw.circle(WIN, HILL, (900, 400), 70)
        # pygame.draw.circle(WIN, INNER_HILL, (900, 400), 50)
        # # Draw holes
        # pygame.draw.circle(WIN, "black", (120, 80), hole_rad)
        # pygame.draw.circle(WIN, "black", (570, 80), hole_rad)
        # pygame.draw.circle(WIN, "black", (900, 400), hole_rad)

        # # Bunkers
        # pygame.draw.circle(WIN, BUNKER, (795, 160), 50)
        # pygame.draw.circle(WIN, BUNKER, (835, 190), 30)
        # pygame.draw.circle(WIN, BUNKER, (600, 635), 130)
        # pygame.draw.circle(WIN, BUNKER, (900, 650), 130)

        # # Inside walls
        # pygame.draw.polygon(WIN, i_wall_c, ((241, 21), (320, 21), (241, 100)))
        # pygame.draw.polygon(WIN, i_wall_c, ((290, 140), (400, 140), (400, 400)))
        # pygame.draw.polygon(WIN, i_wall_c, ((241, 200), (241, 500), (330, 400)))
        # pygame.draw.polygon(WIN, i_wall_c, ((800, 400), (800, 580), (720, 580)))

        # pygame.draw.rect(WIN, i_wall_c, (95, 350, wall_w, wall_h))
        # pygame.draw.rect(WIN, i_wall_c, (21, 200, wall_w, wall_h))

        # # Outside walls
        # pygame.draw.rect(WIN, o_wall_c, (0, 0, 1000, 20))
        # pygame.draw.rect(WIN, o_wall_c, (0, 20, 20, 560))
        # pygame.draw.rect(WIN, o_wall_c, (0, 580, 1000, 20))
        # pygame.draw.rect(WIN, o_wall_c, (980, 20, 20, 560))
        # pygame.draw.rect(WIN, o_wall_c, (220, 20, 20, 560))
        # pygame.draw.rect(WIN, o_wall_c, (400, 140, 20, 440))
        # pygame.draw.rect(WIN, o_wall_c, (420, 140, 200, 20))
        # pygame.draw.rect(WIN, o_wall_c, (620, 20, 20, 400))
        # pygame.draw.rect(WIN, o_wall_c, (800, 160, 20, 420))

        # # Bouncy walls
        # pygame.draw.rect(WIN, PINK, (410, 440, 15, 151))
        # pygame.draw.polygon(WIN, PINK, ((425, 440), (425, 590), (480, 590)))
        
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

        distance_to_hill = math.hypot(ball.body.position.x - 900, ball.body.position.y - 400)

        if distance_to_hill < 70:
            pushDir1 = math.atan2(ball.body.position[1] - 400, ball.body.position[0] - 900)
            pushSpeed += pushSpeedAdd
            if 0 < pushDir1 < 1.57:
                ball.body.velocity += Vec2d(pushSpeed, 0)
                ball.body.velocity += Vec2d(0, pushSpeed)
            elif 1.57 < pushDir1 < math.pi:
                ball.body.velocity -= Vec2d(pushSpeed, 0)
                ball.body.velocity += Vec2d(0, pushSpeed)
            elif -1.57 < pushDir1 < 0:
                ball.body.velocity += Vec2d(pushSpeed, 0)
                ball.body.velocity -= Vec2d(0, pushSpeed)
            elif -1.57 > pushDir1 > -math.pi:
                ball.body.velocity -= Vec2d(pushSpeed, 0)
                ball.body.velocity -= Vec2d(0, pushSpeed)
        else:
            pushSpeed = 0

        # Check if ball is in bunker
        for b in bunkers:
            distance_to_bunker = math.hypot(ball.body.position.x - b[0], ball.body.position.y - b[1])
            if distance_to_bunker <= b[2] - player_radius:
                in_bunker = True
                ball.body.velocity *= 0.4
            else:
                in_bunker = False

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                start_game = False
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    
pygame.quit()