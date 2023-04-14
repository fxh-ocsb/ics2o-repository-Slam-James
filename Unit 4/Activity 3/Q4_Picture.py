# Samuel James
# NAME OF THE PROGRAM:  
# DATE OF CREATION:  
# PURPOSE OF PROGRAM:  



import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('black'))

# draw pacman
draw.circle(gameDisplay, Color('gold'), (250, 250), 250)

draw.polygon(gameDisplay, Color('black'), [(1, 150), (250, 250), (1, 350)])

draw.circle(gameDisplay, Color ('white'), (1,250), 20)
draw.circle(gameDisplay, Color ('white'), (100,250), 20)
draw.circle(gameDisplay, Color ('white'), (200,250), 20)


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