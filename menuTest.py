#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:15:36 2018

@author: jaymz
"""

import pygame
import numpy as np
pygame.init()

from menu import Menu

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

PI = np.pi

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test")

# Loop until the user clicks the close button.
done = False

#----------Functions to "do things"-----------
def f1():
    print("Did a thing!")
def f2():
    print("Did another thing!")

menuEntries = ['Do a Thing', 'Do another thing', 'Do nothing']

inputMenu = Menu( [300,300], menuEntries)
inputMenu.assignFunction(0,f1)
inputMenu.assignFunction(1,f2)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        inputMenu.processMouseInput(event)
        
        if event.type == pygame.QUIT:
            print("User asked to quit.")           
            done = True # Flag that we are done so we exit this loop  
            
 
    # --- Drawing code should go here
    screen.fill(WHITE)
    
    inputMenu.draw(screen)
 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
        
pygame.quit()