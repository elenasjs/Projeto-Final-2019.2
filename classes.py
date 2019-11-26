# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:19:05 2019

@author: elena
"""

import pygame
from init import BLACK, WIDTH, HEIGHT, img_dir, snd_dir, fnt_dir, WHITE, path
import random

# Classe Player 
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe
    def __init__(self, carro):
        
     
        pygame.sprite.Sprite.__init__(self)
              
        self.carro = carro        
        
        self.frame = 0
        self.image = self.carro[self.frame]
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 200
        
        # Velocidade do carrinho
        self.speedx = 0
                 
        # are de colisao
        self.radius = 11

        self.last_update = pygame.time.get_ticks()

    
    # atualiza a posição do carrinho
    def update(self):
        self.rect.x += self.speedx

        # para ficar dentro da tela
        if self.rect.right > 520:
            self.rect.right = 520
        if self.rect.left < 83:
            self.rect.left = 83
        
        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:

            self.last_update = now

            self.frame += 1
            if self.frame == len(self.carro):
                self.frame = 0
            center = self.rect.center
            self.image = self.carro[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

    # carrinhos inimigos
class Mob(pygame.sprite.Sprite):
    
    def __init__(self, policia):
        
        pygame.sprite.Sprite.__init__(self)
        
        # animação do MOB
        self.policia = policia        
        
        # colocando a primeira imagem na tela.
        self.frame = 0
        self.image = self.policia[self.frame]
        
        # o posicionamento.
        self.rect = self.image.get_rect()
        
        # um lugar inicial em x
        i = random.randrange(0,10)
        if i <= 2:
            self.rect.x = 105
        elif i <= 4:
            self.rect.x = 195
        elif i <= 6:
            self.rect.x = 275
        elif i <= 8:
            self.rect.x = 365
        elif i <= 10:
            self.rect.x = 455
        
        # lugar inicial em y
        self.rect.y = random.randrange(-150, -100)
        # uma velocidade inicial
        self.speedx = 0
        self.speedy = 9

        #movimento aos lados do carrinho
        self.direction = 0 # -1 0 +1
        self.direction_count = 0
        self.reference = 0
        
        # colisão estabelecendo um espaco
        self.radius = int(self.rect.width * .85 / 2)

        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 80
        
    # atualiza a posição do carrinho
    def update(self):

        # movimento para os lados
        if self.direction_count == 0:
            self.direction = random.randrange(3)-1
            self.direction_count=100
        self.direction_count -= 1
        
        if self.rect.x <= 100 and self.direction < 0:
            self.direction = 0
        if self.rect.x >= 455 and self.direction > 0:
            self.direction = 0

        if abs(self.reference) >= 85:
            self.direction=0

        self.rect.x += self.direction * 2
        self.reference += self.direction * 2

        self.rect.y += self.speedy

        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.policia):
                self.frame = 0
            center = self.rect.center
            self.image = self.policia[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

        # não deixa sair da pista
        if self.rect.right > 520:
            self.rect.right = 520
        if self.rect.left < 90:
            self.rect.left = 90
        
        # volta para cima e é sorteada uma posição novamente
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:

            i=random.randrange(0,10)
            if i <=2:
                self.rect.x = 105
            elif i <=4:
                self.rect.x = 195
            elif i <=6:
                self.rect.x = 275
            elif i <= 8:
                self.rect.x = 365
            elif i <=10:
                self.rect.x = 455

            self.rect.y = random.randrange(-150, -100)
            if i % 2 == 0:
                self.speedx = 50
            else:
                self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(10, 15)
            self.reference=0


# classe mais
class Mais(pygame.sprite.Sprite):
    # construtor da classe.
    def __init__(self, imagem_mais):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        #animação da mais
        self.imagem_mais = imagem_mais        
        
        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0
        self.image = self.imagem_mais[self.frame]
        
        # sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # lugar inicial em x
        posicao_inicial=[100,195,280,365,455]
        i=random.randrange(0,5)
        self.rect.x = posicao_inicial[i]
        # lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # uma velocidade inicial
        self.speedx = 0
        self.speedy = 3
        
        # estabelecendo um espaco
        self.radius = int(self.rect.width * 85 / 2)
        
        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 120

    def update(self):
        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:

            self.last_update = now

            self.frame += 1
            if self.frame == len(self.imagem_):mais
            self.frame = 0
            
            center = self.rect.center
            self.image = self.imagem_mais[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
              
        self.rect.x += 0
        self.rect.y += self.speedy
        
        # Se a mais passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            posicao_inicial=[100,195,280,365,455]
            i=random.randrange(0,5)
            self.rect.x = posicao_inicial[i]
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = 3

# classe caixa que representa as caixinhas
class Caixa(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, caixa_img):
        
        # Construtor da classe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem.
        self.image = caixa_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(caixa_img, (35, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        posicao_inicial=[100,195,280,365,455]
        i=random.randrange(0,10)
        if i <= 2:
            self.rect.x = posicao_inicial[0]
        elif i <= 4:
            self.rect.x = posicao_inicial[1]
        elif i <=6:
            self.rect.x = posicao_inicial[2]
        elif i<=8:
            self.rect.x = posicao_inicial[3]
        elif i <=10:
            self.rect.x = posicao_inicial[4]
        
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 2
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição da caixa
    def update(self):
        self.rect.x += 0
        self.rect.y += self.speedy
        
        if self.rect.right > 520:
            self.rect.right = 520
        if self.rect.left < 90:
            self.rect.left = 90
        
        # Se a caixa passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            
            posicao_inicial=[100,195,280,365,455]
            i=random.randrange(0,10)
            if i <= 2:
                self.rect.x = posicao_inicial[0]
            elif i <= 4:
                self.rect.x = posicao_inicial[1]
            elif i <=6:
                self.rect.x = posicao_inicial[2]
            elif i<=8:
                self.rect.x = posicao_inicial[3]
            elif i <=10:
                self.rect.x = posicao_inicial[4]
                
            self.rect.y = random.randrange(-100, -40)
            self.speedx = 0
            self.speedy = 2

        
# Classe que representa os tiros
class Tiro(pygame.sprite.Sprite):
    
    # Construtor da classe
    def __init__(self, tiro_img, x, y):
        
        # Construtor da classe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        # imagem de fundo.
        self.image = tiro_img
        
        #posicionamento.
        self.rect = self.image.get_rect()
        
        # lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    # atualiza a posição do tiro
    def update(self):
        self.rect.y += self.speedy