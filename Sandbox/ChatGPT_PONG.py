import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the colors
bg_color = (0, 0, 0)  # black background
paddle_color = (255, 255, 255)  # white paddles
ball_color = (255, 255, 255)  # white ball

# Set the paddle properties
paddle_width = 10
paddle_height = 100

# Set the player 1 properties
player1_x = 50
player1_y = screen_height // 2 - paddle_height // 2

# Set the player 2 properties
player2_x = screen_width - 50 - paddle_width
player2_y = screen_height // 2 - paddle_height // 2

# Set the ball properties
ball_size = 10
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2
ball_dx = random.choice([-5, 5])
ball_dy = random.choice([-5, 5])

# Set the font
font = pygame.font.SysFont(None, 48)

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill the background color
    screen.fill(bg_color)

    # Draw the paddles
    pygame.draw.rect(screen, paddle_color, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, paddle_color, (player2_x, player2_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_size)

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce the ball off the top and bottom of the screen
    if ball_y < 0 or ball_y > screen_height - ball_size:
        ball_dy = -ball_dy

    # Bounce the ball off the paddles
    if ball_x < player1_x + paddle_width and ball_y + ball_size > player1_y and ball_y < player1_y + paddle_height:
        ball_dx = -ball_dx
    elif ball_x > player2_x - ball_size and ball_y + ball_size > player2_y and ball_y < player2_y + paddle_height:
        ball_dx = -ball_dx

    # Update the screen
    pygame.display.update()

    # Cap the FPS
    clock.tick(60)