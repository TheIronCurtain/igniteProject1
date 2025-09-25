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