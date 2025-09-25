import pygame
import random
import sys

pygame.init()

#game settings 
WIDTH, HEIGHT = 600, 800
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 50,30
ROCK_WIDTH, ROCK_HEIGHT = 40,40
ROCK_SPEED = 5
SPAWN_RATE = 30

# next is colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PLAYER_COLOR = (0,200,255)
ROCK_COLOR = (200,50,50)

#screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Dodge the Falling Rocks! ")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# player setup
player = pygame.Rect(WIDTH // 2, HEIGHT - 60, PLAYER_WIDTH, PLAYER_HEIGHT)
player_speed = 8


#rock list
rocks = []
score = 0
frame_count = 0
game_over = False

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def spawn_rock():
    x = random.randint(0, WIDTH - ROCK_WIDTH)
    rock = pygame.Rect(x, 0, ROCK_WIDTH, ROCK_HEIGHT)
    rocks.append(rock)

def reset_game():
    global rocks, score, frame_count, game_over, player
    rocks = []
    score = 0
    frame_count = 0
    game_over = False
    player.x = WIDTH // 2

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Spawn rocks
        frame_count += 1
        if frame_count % SPAWN_RATE == 0:
            spawn_rock()

        # Move and draw rocks
        for rock in rocks[:]:
            rock.y += ROCK_SPEED
            pygame.draw.rect(screen, ROCK_COLOR, rock)

            if rock.colliderect(player):
                game_over = True
            elif rock.top > HEIGHT:
                rocks.remove(rock)
                score += 1

# Draw player
        pygame.draw.rect(screen, PLAYER_COLOR, player)

        # Draw score
        draw_text(f"Score: {score}", 10, 10)

    else:
        # Game over screen
        draw_text("💀 GAME OVER 💀", WIDTH // 2 - 120, HEIGHT // 2 - 40)
        draw_text(f"Final Score: {score}", WIDTH // 2 - 90, HEIGHT // 2)
        draw_text("Press R to restart or Q to quit", WIDTH // 2 - 150, HEIGHT // 2 + 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
        if keys[pygame.K_q]:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()