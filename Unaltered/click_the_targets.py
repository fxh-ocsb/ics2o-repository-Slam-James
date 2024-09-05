import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
TARGET_SIZE = 64  # Size of the target image
NUM_TARGETS = 5   # Number of targets to appear at any given time
TIMER_DURATION = 30  # Timer duration in seconds
RESTART_BUTTON_WIDTH = 200
RESTART_BUTTON_HEIGHT = 50
RESTART_BUTTON_TEXT_COLOR = (255, 0, 255)  # Pink

# Colors
BACKGROUND_COLOR = (255, 255, 255)  # White background

# Load Images and Sounds
background_image = pygame.image.load('background.jpg')
target_images = [pygame.image.load(f'target.png') for i in range(1, 4)]
target_images = [pygame.transform.scale(img, (TARGET_SIZE, TARGET_SIZE)) for img in target_images]

hit_sound = pygame.mixer.Sound('hit_sound.mp3')
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # Loop indefinitely

# Screen Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Click the Targets')

# Game Variables
score = 0
targets = []
current_target_images = []
particles = []
timer = TIMER_DURATION
timer_font = pygame.font.SysFont(None, 48)
score_font = pygame.font.SysFont(None, 36)
restart_button_rect = pygame.Rect(SCREEN_WIDTH - RESTART_BUTTON_WIDTH - 10,
                                  10,
                                  RESTART_BUTTON_WIDTH,
                                  RESTART_BUTTON_HEIGHT)

def initialize_targets():
    global targets, current_target_images
    targets = []
    current_target_images = []
    for _ in range(NUM_TARGETS):
        x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)
        targets.append(pygame.Rect(x, y, TARGET_SIZE, TARGET_SIZE))
        current_target_images.append(int(random.uniform(0, len(target_images))))

def reset_game():
    global score, timer, particles
    score = 0
    timer = TIMER_DURATION
    particles = []
    initialize_targets()

reset_game()

# Game Clock
clock = pygame.time.Clock()

# Main Game Loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if restart_button_rect.collidepoint(mouse_x, mouse_y):
                reset_game()
            else:
                for i, target in enumerate(targets):
                    if target.collidepoint(mouse_x, mouse_y):
                        score += 1
                        targets[i] = pygame.Rect(random.randint(0, SCREEN_WIDTH - TARGET_SIZE), 
                                                random.randint(0, SCREEN_HEIGHT - TARGET_SIZE), 
                                                TARGET_SIZE, TARGET_SIZE)
                        current_target_images[i] = int(random.uniform(0, len(target_images)))
                        hit_sound.play()

                        # Create particles
                        for _ in range(20):
                            particles.append({
                                'position': [mouse_x, mouse_y],
                                'velocity': [random.uniform(-5, 5), random.uniform(-5, 5)],
                                'radius': random.uniform(5, 10),
                                'color': (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                            })

    # Clear Screen
    screen.blit(background_image, (0, 0))

    # Draw Targets
    for i, target in enumerate(targets):
        screen.blit(target_images[current_target_images[i]], target.topleft)

    # Draw Particles
    new_particles = []
    for p in particles:
        pygame.draw.circle(screen, p['color'], (int(p['position'][0]), int(p['position'][1])), int(p['radius']))
        p['position'][0] += p['velocity'][0]
        p['position'][1] += p['velocity'][1]
        p['radius'] -= 0.1
        if p['radius'] > 0:
            new_particles.append(p)
    particles = new_particles

    # Draw Timer
    timer_text = timer_font.render(f'Time: {int(timer)}', True, (255, 0, 255))
    timer_text_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    screen.blit(timer_text, timer_text_rect)

    # Draw Score
    score_text = score_font.render(f'Score: {score}', True, (255, 0, 255))
    screen.blit(score_text, (10, 10))

    # Draw Restart Button (without background)
    restart_text = score_font.render('Restart', True, RESTART_BUTTON_TEXT_COLOR)
    screen.blit(restart_text, (restart_button_rect.x + (RESTART_BUTTON_WIDTH - restart_text.get_width()) // 2,
                                restart_button_rect.y + (RESTART_BUTTON_HEIGHT - restart_text.get_height()) // 2))

    # Update Display
    pygame.display.flip()

    # Update Timer
    if timer > 0:
        timer -= clock.get_time() / 1000  # Subtract time since last frame (in seconds)
    else:
        timer = 0
        # Display a "Game Over" message
        screen.fill(BACKGROUND_COLOR)
        game_over_text = score_font.render('Game Over! Click Restart to play again.', True, (0, 0, 0))
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, 
                                     (SCREEN_HEIGHT - game_over_text.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait 3 seconds before allowing restart
        reset_game()

    # Frame Rate
    clock.tick(30)

pygame.quit()
