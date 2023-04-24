import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
bg_color = (255, 255, 255) # White

# Set the colors and size for the circles
circle_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] # Red, green, blue
circle_radius = 50

# Set the speed and direction for the circles
circle_speed = 5
circle_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

# Create a list of circles
circles = []
for i in range(10):
    color = random.choice(circle_colors)
    x = random.randint(circle_radius, screen_width - circle_radius)
    y = random.randint(circle_radius, screen_height - circle_radius)
    dx, dy = random.choice(circle_directions)
    circles.append({'color': color, 'x': x, 'y': y, 'dx': dx, 'dy': dy})

# Set the frames per second for the screen
fps = 30
clock = pygame.time.Clock()

# Run the screensaver
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the positions of the circles
    for circle in circles:
        circle['x'] += circle_speed * circle['dx']
        circle['y'] += circle_speed * circle['dy']
        if circle['x'] < circle_radius or circle['x'] > screen_width - circle_radius:
            circle['dx'] *= -1
        if circle['y'] < circle_radius or circle['y'] > screen_height - circle_radius:
            circle['dy'] *= -1

    # Draw the circles and update the screen
    screen.fill(bg_color)
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], (circle['x'], circle['y']), circle_radius)
    pygame.display.update()

    # Wait for the next frame
    clock.tick(fps)