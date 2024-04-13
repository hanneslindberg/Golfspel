import pygame
import sys

# Initiera Pygame
pygame.init()

# Skapa en skärm
skärm_bredd = 800
skärm_höjd = 600
skärm = pygame.display.set_mode((skärm_bredd, skärm_höjd))
pygame.display.set_caption("Triangel")

# Definiera färg
vit = (255, 255, 255)
röd = (255, 0, 0)

# Triangelns hörnkoordinater
triangel = [(200, 300), (400, 100), (600, 300)]

# Huvudloop
kör = True
while kör:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kör = False

    # Rensa skärmen
    skärm.fill(vit)

    # Rita triangeln
    pygame.draw.polygon(skärm, röd, triangel)

    # Uppdatera skärmen
    pygame.display.flip()

# Avsluta Pygame
pygame.quit()
sys.exit()
