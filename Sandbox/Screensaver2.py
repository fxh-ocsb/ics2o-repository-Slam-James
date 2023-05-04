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
line_color = (255, 255, 255)  # white lines
circle_color = (255, 255, 255)  # white circles

# Set the properties
num_circles = 10
circle_radius = 50
circle_speed = 2
line_width = 3

# Set the circles
circles = []
for i in range(num_circles):
    x = random.randint(circle_radius, screen_width - circle_radius)
    y = random.randint(circle_radius, screen_height - circle_radius)
    dx = random.choice([-circle_speed, circle_speed])
    dy = random.choice([-circle_speed, circle_speed])
    circles.append((x, y, dx, dy))

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

    # Draw the lines
    for i in range(0, screen_width, 20):
        pygame.draw.line(screen, line_color, (i, 0), (i, screen_height), line_width)
    for i in range(0, screen_height, 20):
        pygame.draw.line(screen, line_color, (0, i), (screen_width, i), line_width)

    # Draw the circles
    for i, circle in enumerate(circles):
        x, y, dx, dy = circle
        pygame.draw.circle(screen, circle_color, (x, y), circle_radius)
        x += dx
        y += dy
        if x - circle_radius < 0 or x + circle_radius > screen_width:
            dx = -dx
        if y - circle_radius < 0 or y + circle_radius > screen_height:
            dy = -dy
        circles[i] = (x, y, dx, dy)

    # Update the screen
    pygame.display.update()

    # Cap the FPS
    clock.tick(60)

