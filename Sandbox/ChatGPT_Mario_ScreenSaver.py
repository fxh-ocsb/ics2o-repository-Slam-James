import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the colors
bg_color = (0, 0, 0)  # black background
circle_color = (255, 255, 255)  # white circle

# Set the circle properties
circle_radius = 30
circle_x = screen_width // 2
circle_y = screen_height // 2
circle_dx = 0
circle_dy = 0

# Set the clock
clock = pygame.time.Clock()

# Run the game
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the circle
    circle_x += circle_dx
    circle_y += circle_dy

    # Keep the circle on the screen
    if circle_x < circle_radius:
        circle_x = circle_radius
    elif circle_x > screen_width - circle_radius:
        circle_x = screen_width - circle_radius

    if circle_y < circle_radius:
        circle_y = circle_radius
    elif circle_y > screen_height - circle_radius:
        circle_y = screen_height - circle_radius

    # Draw the screen
    screen.fill(bg_color)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update the display
    pygame.display.flip()

    # Set the framerate
    clock.tick(60)

    # Set the circle's movement based on keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_dx = -5
    elif keys[pygame.K_RIGHT]:
        circle_dx = 5
    else:
        circle_dx = 0

    if keys[pygame.K_UP]:
        circle_dy = -5
    elif keys[pygame.K_DOWN]:
        circle_dy = 5
    else:
        circle_dy = 0