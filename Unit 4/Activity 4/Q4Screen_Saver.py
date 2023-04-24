#Created: April 2023
#Screen_Saver
#pygame animation using nested loops

import pygame

from pygame import Color
from pygame import draw
from pygame import display
from pygame import time

SCREEN_SIZE = (500, 500)
center_x = 250
center_y = 150

# initialize pygame modules
pygame.init()

clock = time.Clock()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for i in range (0, 100):
        # white background
        gameDisplay.fill(Color('black'))

        # simple animation - ball
        draw.circle(gameDisplay, Color('white'), (center_x, center_y), 30)

        # show the graphics on the screen
        display.flip()

        # get ready for next frame - move the ball down and to the right
        center_x += 1
        center_y += 1

        # delay the program to obtain 60 frames per second
        clock.tick(60)

    for i in range (0, 100):
        # white background
        gameDisplay.fill(Color('white'))

        # simple animation - ball
        draw.circle(gameDisplay, Color('black'),(center_x, center_y), 30)

        # show the graphics on the screen
        display.flip()

        # get ready for next frame - move the ball down and to the left
        center_x -= 1
        center_y += 1

        # delay the program to obtain 60 frames per second
        clock.tick(60)

    for i in range (0, 100):
        # white background
        gameDisplay.fill(Color('black'))

        # simple animation - ball
        draw.circle(gameDisplay, Color('white'),(center_x, center_y), 30)

        # show the graphics on the screen
        display.flip()

        # get ready for next frame -- move the ball up and to the left
        center_x -= 1
        center_y -= 1

        # delay the program to obtain 60 frames per second
        clock.tick(60)

    for i in range (0, 100):
        # white background
        gameDisplay.fill(Color('white'))

        # simple animation - ball
        draw.circle(gameDisplay, Color('black'), (center_x, center_y), 30)

        # show the graphics on the screen
        display.flip()

        # get ready for next frame - - move the ball up and to the right
        center_x += 1
        center_y -= 1

        # delay the program to obtain 60 frames per second
        clock.tick(60)
# Quit Pygame
pygame.quit()