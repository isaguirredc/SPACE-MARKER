import pygame
import tkinter as tk
from tkinter import simpledialog

pygame.init()

# definções básicas
branco = (255,255,255)
preto = (0,0,0)
tamanho = (800, 600)
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode(tamanho)
bg = pygame.image.load("assets/bg.jpg")
icon = pygame.image.load("assets/icon.png")
track = pygame.mixer.Sound("assets/soundtrack.mp3")
foguete = pygame.image.load("assets/foguete.jpg")
relogio = pygame.time.Clock()
pygame.mixer.Sound.play(track)
pygame.display.set_caption('SPACE MARKER!')
pygame.display.set_icon(icon)
fonte = pygame.font.SysFont("dinprobold",28)
fonte_titulo = pygame.font.SysFont("dinprobold", 80)
fonte_instrucao = pygame.font.SysFont("dinprobold", 30)

# tela de início
def tela_inicio():
    tela.blit(foguete, (0, 0))
    
    #texto do título
    texto_titulo = fonte_titulo.render("SPACE MARKER", True, branco)
    rect_titulo = texto_titulo.get_rect(center=(largura_tela/2, altura_tela/10))
    tela.blit(texto_titulo, rect_titulo)
    
    #texto de instrução
    texto_instrucao = fonte_instrucao.render("(PRESSIONE QUALQUER TECLA PARA COMEÇAR)", True, preto)
    rect_instrucao = texto_instrucao.get_rect(center=(largura_tela/2, altura_tela/1.1))
    tela.blit(texto_instrucao, rect_instrucao)
    
    pygame.display.update()

# defs para as bolinhas e nome, comandos de teclado e distância entre cada estrela
def circulos (circles, mouse_pos):
    nome_estrela = asknome()
    circles.append((mouse_pos, nome_estrela))
    comandos(circles)
    if len(circles) > 1:
        linha(circles[-2][0], circles[-1][0])

def marcacao (texto, fonte, cor, posicao):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = posicao
    tela.blit(texto_surface, texto_rect)

def comandos (circles):
    tela.blit(bg, (0, 0))
    marcacao("APERTE F9 PARA APAGAR TODAS AS MARCAÇÕES", fonte_instrucao, branco, (271, 20))
    marcacao("APERTE F10 PARA SALVAR AS MARCAÇÕES ATUAIS", fonte_instrucao, branco, (275, 40))
    marcacao("APERTE F11 PARA CARREGAR AS MARCAÇÕES SALVAS", fonte_instrucao, branco, (292, 60))

    distancia_total = 0 

    for i in range(len(circles)):
        pos, name = circles[i]
        pygame.draw.circle(tela, (branco), pos, 5)
        font = pygame.font.Font(None, 20)
        name_text = font.render(name, True, (branco))
        tela.blit(name_text, (pos[0], pos[1] + 10))

        if i > 0:
            distancia = pygame.math.Vector2(pos).distance_to(circles[i - 1][0])
            distancia_total += distancia
    if len(circles) > 1:
        for i in range(len(circles) - 1):
            start_pos = circles[i][0]
            end_pos = circles[i + 1][0]
            linha(start_pos, end_pos)
            line_distance = pygame.math.Vector2(end_pos).distance_to(start_pos)
            line_text = font.render(f"DISTÂNCIA: {line_distance:.2f}", True, (branco))
            line_pos = (start_pos[0] + (end_pos[0] - start_pos[0]) // 2,
                        start_pos[1] + (end_pos[1] - start_pos[1]) // 2)
            tela.blit(line_text, line_pos)

    pygame.display.update()

def linha(start_pos, end_pos):
    pygame.draw.line(tela, branco, start_pos, end_pos, 1)

def asknome():
    root = tk.Tk()
    root.withdraw()
    name = tk.simpledialog.askstring("☆", "INSIRA O NOME DA ESTRELA:")
    return name if name else "UNKNOWN"

# save e load
def salvar (circles):
    with open("circles.txt", "w") as file:
        for pos, name in circles:
            file.write(f"{pos[0]},{pos[1]},{name}\n")

def carregar():
    circles = []
    try:
        with open("circles.txt", "r") as file:
            for line in file:
                x, y, name = line.strip().split(",")
                pos = (int(x), int(y))
                circles.append((pos, name))
        return circles
    except:
        with open('circles.txt', 'w') as file:
            pass

def main():
    circles = []
    running = True
    tela_inicio_ativa = True
    game_mode = False
    
    while running:
        if tela_inicio_ativa:
            tela_inicio()
        elif game_mode:
            comandos(circles)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if len(circles) > 0:
                    salvar(circles)
                running = False
            if event.type == pygame.KEYDOWN:
                if tela_inicio_ativa:
                    tela_inicio_ativa = False
                    game_mode = True
                else:
                    if event.key == pygame.K_F9:
                        circles = []
                    if event.key == pygame.K_F10:
                        salvar(circles)
                    if event.key == pygame.K_F11:
                        circles = carregar()
            if event.type == pygame.MOUSEBUTTONDOWN and game_mode:
                circulos(circles, pygame.mouse.get_pos())

        pygame.display.update()
        relogio.tick(60)

main()
