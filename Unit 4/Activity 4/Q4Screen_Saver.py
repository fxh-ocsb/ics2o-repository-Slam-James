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
ball_color = (255, 255, 255)  # white ball

# Set the ball properties
ball_radius = 30
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = random.randint(ball_radius, screen_height - ball_radius)
ball_dx = random.randint(-5, 5)
ball_dy = random.randint(-5, 5)

# Set the clock
clock = pygame.time.Clock()

# Run the screensaver
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce the ball off the walls
    if ball_x < ball_radius or ball_x > screen_width - ball_radius:
        ball_dx = -ball_dx
    if ball_y < ball_radius or ball_y > screen_height - ball_radius:
        ball_dy = -ball_dy

    # Draw the ball
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Set the framerate
    clock.tick(60)
        # delay the program to obtain 60 frames per second
    