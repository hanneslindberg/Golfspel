import pygame

# Initiate pygame
pygame.init()

# Create window
BG = pygame.image.load("img/bg.png")
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    clock.tick(FPS)

    # Draw background
    WIN.blit(BG, (0, 0))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    
pygame.quit()