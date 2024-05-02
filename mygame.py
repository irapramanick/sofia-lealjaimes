import pygame
import pygame.font
import random

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sofia's Game")

player = pygame.Rect((random.randint(0, 800), 150, 50, 50))
house_base = pygame.Rect((random.randint(0, 800), 500, 100, 80))

# Create the font
font = pygame.font.SysFont(None, 25)

# Inintialize
is_game_running = True
game_score = 0
miss_score = 0
print(game_score, miss_score)

clock = pygame.time.Clock()

collided = False

while is_game_running:
    clock.tick(60)
    
    text = font.render(str(game_score), True, (255,255,255))
    screen.blit(text, (900,20))
    
    screen.fill((0, 0, 0))
    # If collision happened, draw a new player
    if collided == True:
        player = pygame.Rect((random.randint(0, 800), 150, 50, 50))
        collided = False
        house_base.x = random.randint(0, 800)

    if player.y > 600:
        miss_score += 1
        print(game_score, miss_score)
        player = pygame.Rect((random.randint(0, 800), 150, 50, 50))
    
    pygame.draw.rect(screen, (173, 216, 230), player)
    pygame.draw.rect(screen, (255, 192, 203), house_base)
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(+1, 0)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, +1)
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1)

    # Write code below for moving the house_base across the screen
    house_base.move_ip(+1, 0)
    if house_base.x > 1000:
        house_base.x = 0
        
    # Code for deyecting collision between player and house base
    if player.colliderect(house_base) and collided == False:
        game_score += 1
        print(game_score, miss_score)
        collided = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        
    pygame.display.update()
    

pygame.quit()
