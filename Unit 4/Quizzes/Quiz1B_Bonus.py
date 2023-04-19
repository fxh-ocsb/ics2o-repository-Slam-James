# Samuel James
# Quiz1B_Bonus  
# April 19, 2023  
# To find dimensions of a shape

import random
import pygame
import math


from pygame import Color, Rect
from pygame import draw
from pygame import display

Pixels = random.randint(300, 400)
Length = random.randint(100, 150)
percent_value = random.randint(30, 50)
True_number = percent_value / 100


Position = Pixels * True_number

SCREEN_SIZE = (Pixels, Pixels)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('black'))

# draw pacman
draw.rect(gameDisplay, Color('gold'), [(Position), (Position), (Position), (Position)])


Rounded_Position = "{:.2f}".format(Position)

print("The length of one side of the square is roughly equal to", Rounded_Position, "cm.")

Area = math.pow(Position, 2)
Rounded_Area = "{:.2f}".format(Area)
print("The area of the square is equal to roughly", Rounded_Area, "Centimeters Squared. Thank you for completing this pop quiz!")


# draw a body

# show the graphics on the screen
display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
# Quit Pygame
pygame.quit()