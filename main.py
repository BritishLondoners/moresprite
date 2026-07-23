import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add More Sprites")

# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)   # Blue
ENEMY_COLOR = (255, 0, 0)    # Red

# Player setup
player = pygame.Rect(WIDTH//2 - 25, HEIGHT//2 - 25, 50, 50)

# Enemy setup (7 random positions)
enemies = []
for _ in range(7):
    x = random.randint(0, WIDTH - 40)
    y = random.randint(0, HEIGHT - 40)
    enemies.append(pygame.Rect(x, y, 40, 40))

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Collision detection
    for enemy in enemies[:]:
        if player.colliderect(enemy):
            score += 1
            enemies.remove(enemy)  # Remove collided enemy

    # Fill background
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
