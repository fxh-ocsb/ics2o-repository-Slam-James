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
ball_color = (255, 0, 0)  # red ball

# Set the paddle properties
paddle_width = 10
paddle_height = 100
paddle_speed = 5

# Set the player 1 properties
player1_x = 50
player1_y = screen_height // 2 - paddle_height // 2
player1_dy = 0

# Set the player 2 properties
player2_x = screen_width - 50 - paddle_width
player2_y = screen_height // 2 - paddle_height // 2
player2_dy = 0

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_dy = -paddle_speed
            elif event.key == pygame.K_s:
                player1_dy = paddle_speed
            elif event.key == pygame.K_UP:
                player2_dy = -paddle_speed
            elif event.key == pygame.K_DOWN:
                player2_dy = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player1_dy < 0:
                player1_dy = 0
            elif event.key == pygame.K_s and player1_dy > 0:
                player1_dy = 0
            elif event.key == pygame.K_UP and player2_dy < 0:
                player2_dy = 0
            elif event.key == pygame.K_DOWN and player2_dy > 0:
                player2_dy = 0

    # Move the paddles
    player1_y += player1_dy
    player2_y += player2_dy

    # Keep the paddles on the screen
    if player1_y < 0:
        player1_y = 0
    elif player1_y > screen_height - paddle_height:
        player1_y = screen_height - paddle_height

    if player2_y < 0:
        player2_y = 0
    elif player2_y > screen_height - paddle_height:
        player2_y = screen_height - paddle_height

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce the ball off the top and bottom of the screen
    if ball_y < 0 or ball_y > screen_height - ball_size:
        ball_dy = -ball_dy

    # Bounce the ball off the paddles
    if ball_x < player1_x + paddle_width and ball_y + ball_size > player1_y and ball_y < player1_y + paddle:

            pygame.quit()
            quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.y > 0:
        player1_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player1_paddle.y < screen_height - paddle_height:
        player1_paddle.y += paddle_speed
    if keys[pygame.K_UP] and player2_paddle.y > 0:
        player2_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_paddle.y < screen_height - paddle_height:
        player2_paddle.y += paddle_speed

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Check for collision between ball and walls
    if ball.y < 0 or ball.y > screen_height - ball_size:
        ball_dy = -ball_dy

    # Check for collision between ball and paddles
    if ball.colliderect(player1_paddle):
        ball_dx = ball_speed
        ball_dy = random.randint(-ball_speed, ball_speed)
    elif ball.colliderect(player2_paddle):
        ball_dx = -ball_speed
        ball_dy = random.randint(-ball_speed, ball_speed)

    # Check for score
    if ball.x < 0:
        player2_score += 1
        ball.x = screen_width // 2 - ball_size // 2
        ball.y = screen_height // 2 - ball_size // 2
        ball_dx = ball_speed
        ball_dy = ball_speed
    elif ball.x > screen_width - ball_size:
        player1_score += 1
        ball.x = screen_width // 2 - ball_size // 2
        ball.y = screen_height // 2 - ball_size // 2
        ball_dx = -ball_speed                                  
        ball_dy = ball_speed

    #