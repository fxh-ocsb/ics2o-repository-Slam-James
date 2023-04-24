import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the colors
bg_color = (0, 0, 0)  # black background
player_color = (255, 255, 255)  # white player
platform_color = (255, 0, 0)  # red platform

# Set the player properties
player_size = 50
player_x = screen_width // 2
player_y = screen_height // 2
player_dx = 0
player_dy = 0
player_speed = 5
player_jump_power = 20
player_jump_count = 0
player_jump_limit = 2

# Set the platform properties
platform_width = 200
platform_height = 20
platform_x = 0
platform_y = screen_height - platform_height

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -player_speed
            elif event.key == pygame.K_RIGHT:
                player_dx = player_speed
            elif event.key == pygame.K_UP and player_jump_count < player_jump_limit:
                player_dy = -player_jump_power
                player_jump_count += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_dx < 0:
                player_dx = 0
            elif event.key == pygame.K_RIGHT and player_dx > 0:
                player_dx = 0

    # Move the player
    player_x += player_dx
    player_y += player_dy

    # Apply gravity to the player
    player_dy += 1

    # Keep the player on the screen
    if player_x < player_size // 2:
        player_x = player_size // 2
    elif player_x > screen_width - player_size // 2:
        player_x = screen_width - player_size // 2

    if player_y < player_size // 2:
        player_y = player_size // 2
        player_dy = 0
    elif player_y > screen_height - player_size // 2:
        player_y = screen_height - player_size // 2
        player_dy = 0
        player_jump_count = 0

    # Check for collision between player and platform
    player_rect = pygame.Rect(player_x - player_size // 2, player_y - player_size // 2, player_size, player_size)
    platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
    if player_rect.colliderect(platform_rect):
        player_y = platform_y - player_size // 2
        player_dy = 0
        