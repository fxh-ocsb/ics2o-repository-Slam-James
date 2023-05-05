import pygame
import os

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 1.5
        self.jump_power = -20
        self.on_ground = False
        self.facing_right = True
    
    def update(self):
        # Apply gravity to the player
        self.speed_y += self.gravity
        
        # Move the player horizontally
        self.rect.x += self.speed_x
        
        # Check for collision with walls
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Move the player vertically
        self.rect.y += self.speed_y
        
        # Check for collision with the ground
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.speed_y = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.speed_y > 0 and self.rect.bottom <= platform.rect.top + self.speed_y:
                    self.rect.bottom = platform.rect.top
                    self.speed_y = 0
                    self.on_ground = True
                elif self.speed_y < 0 and self.rect.top >= platform.rect.bottom + self.speed_y:
                    self.rect.top = platform.rect.bottom
                    self.speed_y = 0
    
    def jump(self):
        if self.on_ground:
            self.speed_y = self.jump_power
    
    def move_right(self):
        self.speed_x = 5
        self.facing_right = True
    
    def move_left(self):
        self.speed_x = -5
        self.facing_right = False
    
    def stop(self):
        self.speed_x = 0
    
    def shoot(self):
        if self.facing_right:
            bullet = Bullet(self.rect.right, self.rect.centery, 10)
        else:
            bullet = Bullet(self.rect.left, self.rect.centery, -10)
        bullets.add(bullet)
        all_sprites.add(bullet)

# Set up the platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Set up the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self
