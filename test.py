import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golfspel")

BG = pygame.image.load("bg.png")

player = [WIDTH / 2, HEIGHT / 2]
max_speed = 110
player_radius = 10

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # Begränsar uppdateringshastigheten till 60 FPS

        mx, my = pygame.mouse.get_pos()
        direction_vector = [mx - player[0], my - player[1]]
        length = min(110, math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if length != 0:
                    direction_vector[0] /= length
                    direction_vector[1] /= length
                speed = max_speed * (length / 110)
                new_ball_pos = [player[0] + direction_vector[0] * speed, player[1] + direction_vector[1] * speed]

                # Beräknar antal steg för att nå destinationen
                distance = math.sqrt((new_ball_pos[0] - player[0]) ** 2 + (new_ball_pos[1] - player[1]) ** 2)
                num_steps = int(distance / max_speed) + 1

                for step in range(num_steps):
                    t = step / num_steps  # Andel av avståndet som har färdigställts
                    current_pos = [lerp(player[0], new_ball_pos[0], t), lerp(player[1], new_ball_pos[1], t)]
                    redraw_game_window(current_pos)
                    pygame.time.delay(20)  # Justera detta värde för rörelsens mjukhet

        redraw_game_window()

    pygame.quit()

def lerp(start, end, t):
    return start + (end - start) * t

def redraw_game_window(ball_pos=None):
    WIN.blit(BG, (0, 0))
    pygame.draw.circle(WIN, "black", [800, 100], player_radius)
    if ball_pos:
        pygame.draw.circle(WIN, "white", (int(ball_pos[0]), int(ball_pos[1])), player_radius)
    pygame.display.update()

if __name__ == "__main__":
    main()
