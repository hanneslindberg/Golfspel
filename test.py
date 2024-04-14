import pymunk
import pygame

# Initialisera Pygame och skapa fönstret
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minigolf")

# Skapa Pymunk-rymden
space = pymunk.Space()
space.gravity = (0, 0)  # Ingen gravitation för minigolf

# Skapa ett lager för fältet där bollen kan gå över
def ignore_collision(arbiter, space, data):
    return False

# Lägg till kollisionshanteraren för att ignorera kollisioner mellan lagren
space.add_collision_handler(0, 0).pre_solve = ignore_collision

# Skapa en boll
ball_body = pymunk.Body()
ball_body.position = (400, 300)
ball_shape = pymunk.Circle(ball_body, 20)
ball_shape.elasticity = 0.8  # Exempel: Ange elasticitet för bollen
ball_shape.friction = 0.2  # Exempel: Ange friktion för bollen
space.add(ball_body, ball_shape)

# Skapa en "bunker" (ett fält där bollen kommer att sakta ner)
bunker_body = pymunk.Body(body_type = pymunk.Body.STATIC)
bunker_shape = pymunk.Circle(bunker_body, 50)
bunker_body.position = (400, 300)
bunker_shape.elasticity = 0.5  # Exempel: Ange elasticitet för bunkern
bunker_shape.friction = 1.0  # Exempel: Högre friktion för bunkern
space.add(bunker_body, bunker_shape)

# Spel-loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Uppdatera Pymunk-simuleringen
    space.step(1 / 60)

    # Rita allt
    screen.fill((255, 255, 255))  # Rensa skärmen
    # Rita bunkern
    pygame.draw.circle(screen, (255, 0, 0), (int(bunker_body.position.x), int(bunker_body.position.y)), 50)
    # Rita bollen
    pygame.draw.circle(screen, (0, 0, 255), (ball_body.position.x, ball_body.position.y), 20)
    pygame.display.flip()

    # Begränsa uppdateringshastigheten
    clock.tick(1)

# Avsluta Pygame
pygame.quit()
