pygame.init() 
pygame.mixer.init()
import pygame
import sys
import time
from os import path
import os
import random

# Nome do jogo
pygame.display.set_caption("ToshiRacer")

# Ícone do jogo
icon = pygame.image.load(path.join(img_dir, "principal.png")).convert()
pygame.display.set_icon(icon)

# dicionario img, snd, fnt
assets = load_assets(img_dir, snd_dir, fnt_dir)

# ajuste de velocidade
clock = pygame.time.Clock()

# background
background = pygame.image.load(path.join(img_dir, "pista.jpeg")).convert()
background_rect = background.get_rect()
background_rect_cima = background.get_rect()
background_rect_cima.y = -HEIGHT

# som
boom_sound = assets["batida_sound"]
destroy_sound = assets["batida_sound"]
pew_sound = assets["tiro_sound"]
Ta_Da = assets["caixa_sound"]
moeda = assets["mais_sound"]
os.environ["SDL_VIDEO_CENTERED"] = "1"

from init import img_dir, snd_dir, fnt_dir, BLACK, WIDTH, HEIGHT, FPS, WHITE, YELLOW, bright_YELLOW

from classes import Player, Mob, Caixa, Mais, Tiro

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    assets["tiro_img"] = pygame.image.load(path.join(img_dir, "tiro.png")).convert()
    assets["caixa_img"] = pygame.image.load(path.join(img_dir, "caixa.jpeg")).convert()
    assets["batida_sound"] = pygame.mixer.Sound(path.join(snd_dir, "batida.wav"))
    assets["mais_sound"] = pygame.mixer.Sound(path.join(snd_dir, "mais.wav"))
    assets["batida_sound"] = pygame.mixer.Sound(path.join(snd_dir, "batida.wav"))
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 25)
    return assets

# Cor fonte
def text_object(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

# high score
def maior_pontuacao(pont, nomecolocado):
    RECORDE = get_high_score()
    if pont > RECORDE:
        save_high_score(pont)
        save_nome(nomecolocado)

# le o high score
def get_high_score():
    high_score_file = open("ponto_high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close() 
    return high_score
 
# salvar o maior high score
def save_high_score(new_high_score):
    high_score_file = open("ponto_high_score.txt", "w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()

# salvar o nome da pessoa
def save_nome(nomecolocado):
    nome = open("nome_high_score.txt", "w")
    nome.write(nomecolocado)
    nome.close()

# ler o nome da pessoa do high score
def get_name():
    nome = open("nome_high_score.txt", "r")
    nomee = nome.read()
    nome.close()
    return nomee

# botoes final 
def button(msg, x, y, w, h, inactive, active):

    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, active, (x, y, w, h))
          
    else:
        pygame.draw.rect(screen, inactive, (x, y, w, h))    

    smalltext = pygame.font.Font("freesansbold.ttf", 12)
    textSurf, textRect = text_object(msg, smalltext)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

# tela inicial
def tela_inicial(screen):


    largeText = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 27)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(200, 250, 150, 40)
    color_inactive = WHITE
    color_active = YELLOW
    color = color_inactive
    active = False
    text = ""

    # Imagem de fundo
    background = pygame.image.load(path.join(img_dir, "inicio.png")).convert()
    background_rect_1 = background.get_rect()
    background_rect_2 = background.get_rect()
    background_rect_2.y = -HEIGHT

    done = False
    while not done:
        # o que o usuário fez
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # clicando na caixinha
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False

       
        # Define duas imagens para irem abaixando
        background_rect_2.y += 5
        background_rect_1.y += 5

        if background_rect_1.y >= HEIGHT :
            background_rect_1.y = 0
            background_rect_2.y = -HEIGHT

        # caixinha
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        # Nome
        pedenome, thenew = text_object("INSIRA SEU NOME", largeText)
        thenew.center = ((WIDTH/2),(HEIGHT/2 - 170))
        screen.blit(pedenome, thenew)

        # enter
        ENTER, thenew = text_object("APERTE ENTER", largeText)
        thenew.center = ((WIDTH/2),(HEIGHT/2 - 80))
        screen.blit(ENTER, thenew)

        # maior pontuação e o nome do recordista
        puentos = get_high_score()
        nuemes = get_name()
        poemaior, poe = text_object("RECORDISTA", largeText)
        poe.center = ((WIDTH/2),(HEIGHT/2 - 360))
        screen.blit(poemaior, poe)
        pedenome, thenew = text_object(f"{nuemes}: {puentos}", largeText)
        thenew.center = ((WIDTH/2),(HEIGHT/2 - 330))
        screen.blit(pedenome, thenew)

        pygame.display.flip()
        clock.tick(30)

    # Retorna o nome para utilizar no High Score
    return nomecolocado

# Função da tela final do jogo/batida do carro 
def tela_mostra_pontuacao(screen, nomecolocado, pont):

    # fontes com os tamanhos 
    largeText = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 27)
    maiortext = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 40)
    clock = pygame.time.Clock()

    # todas as informações na tela, junto com a imagem de fundo
    background = pygame.image.load(path.join(img_dir, "tela_inicial.png")).convert()
    background_rect = background.get_rect()
    screen.blit(background, background_rect)

    poetexto, thenew = text_object(f"{nomecolocado}", maiortext)
    thenew.center = ((WIDTH/2),(HEIGHT/2-360))
    screen.blit(poetexto, thenew)

    poetexto2, thenew = text_object("SUA PONTUAÇÃO:", largeText)
    thenew.center = ((WIDTH/2),(HEIGHT/2 - 300))
    screen.blit(poetexto2, thenew)

    poenome, thenew = text_object(f"{pont}", maiortext)
    thenew.center = ((WIDTH/2),(HEIGHT/2 - 250))
    screen.blit(poenome, thenew)

    # Colocando os botões 
    button("RESTART (R)", 180, 540, 75, 50, YELLOW, bright_YELLOW)
    button("QUIT (Q)", 345, 540, 75, 50, WHITE, WHITE)

    # Vendo se a pessoa foi recordista ou não
    maior_pontuacao = get_high_score()
    if pont >= maior_pontuacao:
        poenome, thenew = text_object("O MAIS NOVO", largeText)
        thenew.center = ((WIDTH/2),(HEIGHT/2 - 100))
        screen.blit(poenome, thenew)
        poenome, thenew = text_object("RECORDISTA!", largeText)
        thenew.center = ((WIDTH/2),(HEIGHT/2 - 40))
        screen.blit(poenome, thenew)

    pygame.display.flip()
    clock.tick(30)

    # Coloca ações para os "botões" do final do jogo
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    principal("")
                    done = True
                if event.key == pygame.K_r:
                    principal(nomecolocado) 
                    done = True

        # Carrega a fonte para desenhar o score.
        score_font = assets["score_font"]

        # Cria um carrinho. O construtor será chamado automaticamente. O for é para a animação da roda
        carro=[]
        for i in range(4):
            carrinho = "game_over{}.png".format(i)
            player_img = pygame.image.load(path.join(img_dir, carrinho)).convert()
            player_img = pygame.transform.scale(player_img, (58, 75))
            player_img.set_colorkey(WHITE)
            carro.append(player_img)
        player = Player(carro)

        # Cria todos os sprites e adiciona o player em tal
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        # Cria um grupo só dos carrinhos inimigos. O for é para a animação das rodas
        mobs = pygame.sprite.Group()
        inimigo=[]
        for i in range(4):
            filename = "inimigo{}.png".format(i)
            inimigo_img = pygame.image.load(path.join(img_dir, filename)).convert()
            inimigo_img = pygame.transform.scale(inimigo_img, (58, 75))  
            inimigo_img.set_colorkey(WHITE)
            inimigo.append(inimigo_img)
        
        # grupo para moedas
        mais = pygame.sprite.Group()

        # grupo para caixas
        box = pygame.sprite.Group()


        #grupo de tiros
        tiro = pygame.sprite.Group()

        # cria carrinhos e add em mobs
        for i in range(4):
            m = Mob(inimigo)
            all_sprites.add(m)
            mobs.add(m)
            
        #cria as moedas
        imagem_mais=[]
        for i in range(9):
            filename = "mais{}.png".format(i)
            Mais_img = pygame.image.load(path.join(img_dir, filename)).convert()
            Mais_img = pygame.transform.scale(Mais_img, (35, 35))
            Mais_img.set_colorkey(WHITE)
            imagem_mais.append(Mais_img)

        # adiciona as moedas nos
        c = Mais(imagem_mais)
        all_sprites.add(c)
        mais.add(c)
        
        # define quantos tiros a pessoa começa e quantos pontos
        contagemdetiros = 3
        score = 0
          
        
            nomecolocado = tela_inicial(screen)

        # loop principal
        running = True
        while running:

            # ajusta a velocidade do jogo
            clock.tick(FPS)

    
            # sortear caixinha
            if random.randrange(1, 700) == 1:
                b = Box(assets["box_img"])
                all_sprites.add(b)
                box.add(b)

            # sortear moeda
            if random.randrange(1,500) == 1:
                m = (imagem_mais)
                all_sprites.add(c)
                mais.add(c)
    
            # eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                #  fechado.
                if event.type == pygame.QUIT:
                    running = False
                
                # apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    
                    # dependendo da tecla, altera a velocidade.
                    fator = 0
                    if estanevando or estanevando_tempo > 0:
                        fator = 2
                    if event.key == pygame.K_LEFT:
                        speedx = -5 + fator
                    if event.key == pygame.K_RIGHT:
                        speedx = 5 + fator
                    
                    # se for um espaço, atira! (se tiver)
                    if contagemdetiros > 0:    
                        if event.key == pygame.K_SPACE:
                            tiroo = Tiro(assets["tiro_img"], player.rect.centerx, player.rect.top)
                            all_sprites.add(tiro)
                            tiro.add(tiroo)
                            pew_sound.play()
                            contagemdetiros -= 1
                                      
                # se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    fator = 0
                    if estanevando or estanevando_tempo > 0:
                        fator = 2
                    
            
            # velocidade em x do player (carro)
            player.speedx = speedx
                        
            # se jogador encostou a parede. Se encostar, morre.
            if player.rect.right > 519:
                batida_sound.play()
                running = False
            if player.rect.left < 89:
                batida_sound.play()
                running = False    
            
        
            all_sprites.update()
                
            # se tiro acertou carrinhos
            hits = pygame.sprite.groupcollide(mobs, tiro, True, True)
            for hit in hits:
                #precisa gerar outro
                destroy_sound.play()
                m = Mob(inimigo) 
                all_sprites.add(m)
                mobs.add(m)
                score += 5
            
            # se bater
            hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
            if hits:
                boom_sound.play()
                # Precisa esperar senão fecha duma vez
                time.sleep(0.5)
                running = False
            
            # pegar o mais
            hits = pygame.sprite.spritecollide(player, mais, True, False)
            if hits:
                mais.play()
                score += 10

            # pegar a caixa
            hits = pygame.sprite.spritecollide(player, caixa, True, False)
            for hit in hits:
                Ta_Da.play()
                score += 5
                contagemdetiros += 3
                

            # vai aumentando e estabiliza em 18
            if velocidade < 18:
                velocidade += aceleracao

            # a cada loop, redesenha o fundo e os sprites  
            background_y_cima += velocidade
            background_y += velocidade
    
            if background_y >= HEIGHT:
                background_y = 0
                background_y_cima = -HEIGHT

            background_rect_cima.y = background_y_cima
            background_rect.y = background_y               

            screen.blit(background, background_rect_cima)
            screen.blit(background, background_rect)
            all_sprites.draw(screen)

            # Desenha o score, por tempo
            timee += 1
            pont = (timee//FPS)+score
            text_surface = score_font.render("{:01d}".format(pont), True, BLACK)           
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH-300,  10)
            screen.blit(text_surface, text_rect)

            if contagemdetiros > 0:
                text_surface = score_font.render("SPACE:{:01d} ESPECIAIS".format(contagemdetiros), True, BLACK)
                text_rect = text_surface.get_rect()
                text_rect.midtop = (WIDTH/2,  HEIGHT-130)
                screen.blit(text_surface, text_rect)                

           
            pygame.display.flip()

            # para ver se a pessoa fez a maior pontuação
            maior_pontuacao(pont, nomecolocado)

        # maior pontuador
        maior_pontuacao(pont, nomecolocado)

        # tela final para mostrar a pontuação da pessoa
        tela_mostra_pontuacao(screen, nomecolocado, pont)

        # Matando os mobs e o player para fazê-lo novamente quando voltar o loop
        for mobs in all_sprites:
            mobs.kill()
            player.kill()

# Comando para evitar travamentos.
try: 
    
    principal('')

finally:
    
    pygame.quit()