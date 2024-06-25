import pygame
from tkinter import simpledialog

pygame.init()

# definições básicas
branco = (255,255,255)
preto = (0,0,0)
tamanho = (800, 600)
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode( tamanho )
bg = pygame.image.load("assets/bg.jpg")
icon = pygame.image.load("assets/icon.png")
track = pygame.mixer.Sound("assets/soundtrack.mp3")
relogio = pygame.time.Clock()
pygame.mixer.Sound.play(track)
pygame.display.set_caption('SPACE MARKER!')
pygame.display.set_icon(icon)
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonte_titulo = pygame.font.SysFont("comicsans", 74)
fonte_instrucao = pygame.font.SysFont("comicsans", 36)
foguete = pygame.image.load("assets/foguete.jpg")

#tela de início
def tela_inicio():
    if tela_inicio:
        tela.blit(foguete, (0, 0)) 
    else:
        tela.fill(branco)
    
    #texto do título
    texto_titulo = fonte_titulo.render("Space Marker!", True, preto)
    rect_titulo = texto_titulo.get_rect(center=(largura_tela/2, altura_tela/3))
    tela.blit(texto_titulo, rect_titulo)
    
    #texto de instrução
    texto_instrucao = fonte_instrucao.render("Pressione qualquer tecla para começar", True, preto)
    rect_instrucao = texto_instrucao.get_rect(center=(largura_tela/2, altura_tela/6))
    tela.blit(texto_instrucao, rect_instrucao)
    
    pygame.display.flip()

#Loop principal
inicio = True
while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            inicio = False
    
    tela_inicio()
