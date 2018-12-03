#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:16:01 2018

@author: jaymz
"""

import pygame
import numpy as np

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

SEPSIZE = 20

class Menu:
    def __init__(self, loc, entries, rightClick = False, activated = True):
        self.loc = loc
        self.entries = entries
        self.funcAssignments = [None]*len(entries)
        
        self.rightClickBehavior = rightClick
        
        self.activated = activated
        
        self.font = pygame.font.SysFont('Calibri', 25, True, False)
        
        self.selectedIndex = None
        self.clickedIndex = None
        
        self.width = 200
    
    def draw(self, screen):
        
        if(not self.activated):
            return
        
        N = len(self.entries)
        
        pygame.draw.rect(screen, BLACK, [self.loc[0], self.loc[1] - 2, self.width, SEPSIZE*N], 2)
        
        for i in range(0,N):
            if(self.selectedIndex is not None and i == self.selectedIndex):
                pygame.draw.rect(screen, RED, [self.loc[0], self.loc[1] + SEPSIZE*(i), self.width, SEPSIZE], 0)
            else:
                pygame.draw.rect(screen, BLACK, [self.loc[0], self.loc[1] - 2, self.width, SEPSIZE*N], 2)
            
            text = self.font.render(self.entries[i],True, BLACK)  # True for antialiased text
            screen.blit(text,[self.loc[0] + 5 , self.loc[1] + SEPSIZE * i ])
            
    def getMenuIndex(self, pos):
        N = len(self.entries)
        for i in range(0,N):
            if(      self.loc[0]    <=  pos[0] <= self.loc[0] + self.width
                 and self.loc[1] +2 + SEPSIZE*i <=  pos[1] <= self.loc[1] + SEPSIZE*(i + 1) + 2):
                return i
        return None
                
            
    def processMouseInput(self, event):
        if(event.type == pygame.MOUSEMOTION):
            self.selectedIndex = self.getMenuIndex(pygame.mouse.get_pos())
            
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1 and self.activated):
                index = self.getMenuIndex(pygame.mouse.get_pos())
                if(index is not None):
                    self.clickedIndex  = index
                    self.selectedIndex = None
                    if(self.funcAssignments[index] is not None):
                        self.funcAssignments[index]()
                    else:
                        print("No function assignment for menu entry " + self.entries[index])
                else:
                    self.clickedIndex  = None
                    self.selectedIndex = None
            elif(event.button == 3):
                if(self.rightClickBehavior):
                    self.activated = True
                    self.loc = pygame.mouse.get_pos()
        
        elif(event.type == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                index = self.getMenuIndex(pygame.mouse.get_pos())
                if(index is not None):
                    self.clickedIndex  = None
                    self.selectedIndex = index
                else:
                    self.clickedIndex  = None
                    self.selectedIndex = None
        
        elif(event.type == pygame.KEYDOWN):
            if(self.rightClickBehavior):
                if(event.unicode == '\x1b'):
                    self.activated = False
                    
    def assignFunction(self,menuIndex, func):
        self.funcAssignments[menuIndex] = func
                    
        