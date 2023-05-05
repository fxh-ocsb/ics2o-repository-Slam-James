import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the circle
circle_radius = 20
circle_x = screen_width // 2
circle_y = screen_height // 2

# Set up the movement speed
movement_speed = 0.1

# Set up the colors
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
current_color_index = 0
color_change_interval = 5 # in seconds
last_color_change_time = time.time()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and circle_y - movement_speed > 0:
        circle_y -= movement_speed
    if keys[pygame.K_s] and circle_y + movement_speed < screen_height:
        circle_y += movement_speed
    if keys[pygame.K_a] and circle_x - movement_speed > 0:
        circle_x -= movement_speed
    if keys[pygame.K_d] and circle_x + movement_speed < screen_width:
        circle_x += movement_speed

        
        
    # Check if it's time to change the color
    current_time = time.time()
    if current_time - last_color_change_time > color_change_interval:
        current_color_index = (current_color_index + 1) % len(colors)
        last_color_change_time = current_time
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw the circle with the current color
    current_color = colors[current_color_index]
    pygame.draw.circle(screen, current_color, (circle_x, circle_y), circle_radius)
    
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()