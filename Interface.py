from Combat import *
from pygame import *
import pygame
from Sprites import *
combat1 = Combat() 
combat1.valeursCombat(Ronflex, Rhinoféros)
combat1.typeEtPuissancePokemon1()
combat1.typeEtPuissancePokemon2()
combat1.tableDesTypes()
combat1.degatsPV()
Sprites1 = Sprites()

spritetext = ""

if combat1.pokemon1.getNom() == "Ronflex":
    spritetext

Spritepoke1 = pygame.image.load("Images/snorlaxback.png")
Spritepoke1 = pygame.transform.scale(Spritepoke1, (240,240))

SpritePoke2 = pygame.image.load("Images/rhydon.png")
SpritePoke2 = pygame.transform.scale(SpritePoke2, (240,240))

interfacebas = pygame.image.load("Images/interfacebas.png")
interfacebas = pygame.transform.scale(interfacebas, (800,100))

interfacepvennemi = pygame.image.load("Images/interfacepv.png")
interfacepv = pygame.image.load("Images/interfacepv.png")

icon = pygame.image.load("Images/pokeball.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Devenez le meilleur dresseur !")

pygame.font.init()
font = pygame.font.SysFont("NewTimesRoman", 40)
message = font.render("Que doit faire {} ?".format(combat1.pokemon1.getNom()), True, (0,0,0))


pygame.font.init()
font = pygame.font.SysFont("NewTimesRoman", 40)
pvtop = font.render("PV:" + str(combat1.pokemon1.getPV()) ,True, (0,0,0))
pvbot = font.render("PV:" + str(combat1.pokemon2.getPV()),True, (0,0,0))

pygame.init()
width, height = 800,480
window = pygame.display.set_mode((width, height))
bg_img = pygame.image.load("Images/background.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #En dessous on peut remplacer les pokémons par ceux disponibles écrit au dessus.
    
    
    window.blit(bg_img, (0,0))
    window.blit(Spritepoke1, (20,240))
    window.blit(SpritePoke2, (500,0))
    window.blit(interfacebas, (0,380))
    window.blit(message, (15, 420))
    window.blit(interfacepvennemi, (0,0))
    window.blit(pvtop, (15,15))
    window.blit(interfacepv, (626,283))
    window.blit(pvbot, (641,295))
    
    pygame.display.update()





   


