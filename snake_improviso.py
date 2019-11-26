# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:43:36 2019

@author: elena
"""

import pygame
from pygame.locals import *

UP=0
RIGHT= 1
DOWN= 2
LEFT=3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_captation('Snake')

snake=[(200,200),(210,200),(220,200)]
snake_skin=pygame.Surface((10,10))
snake_skin.fill(255,255,255)

apple= pygame.Surface((10,10))
apple.fill((225,0,0))

my_direction = LEFT

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            
    screen.fill((0,0,0))
    skin.fill(255,255,255)
    skin.fill(255,255,255)
    
    for pos in snake:
        screen.blit(snake_skin,pos)
