# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:19:53 2019

@author: elena
"""

from os import path

# figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img_dir')
snd_dir = path.join(path.dirname(__file__), 'snd_dir')
fnt_dir = path.join(path.dirname(__file__), 'font_dir')


# dados gerais do jogo
WIDTH = 600 # Largura da tela
HEIGHT = 800 # Altura da tela
FPS = 65 # Frames por segundo

# define algumas variáveis com as cores 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
bright_YELLOW = (225, 255, 0)