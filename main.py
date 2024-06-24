import pygame
from tkinter import simpledialog

pygame.init()

# definições básicas
branco = (255,255,255)
preto = (0,0,0)
tamanho = (800, 600)
tela = pygame.display.set_mode( tamanho )
bg = pygame.image.load("assets/bg.jpg")
icon = pygame.image.load("assets/icon.png")
track = pygame.mixer.Sound("assets/soundtrack.mp3")
relogio = pygame.time.Clock()
pygame.mixer.Sound.play(track)
pygame.display.set_caption('SPACE MARKER!')
pygame.display.set_icon(icon)