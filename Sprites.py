import pygame
from pygame import *

class Sprites():

    def Snorlaxback():
        Snorlaxb = pygame.image.load("Images/snorlaxback.png")
        Snorlaxb = pygame.transform.scale(Snorlaxb, (240,240))

    def Snorlaxfront():
        Snorlaxf = pygame.image.load("Images/snorlax.png")
        Snorlaxf = pygame.transform.scale(Snorlaxf, (240,240))

    def Arcanineback():
        Arcanineb = pygame.image.load("Images/arcanineback.png")
        Arcanineb = pygame.transform.scale(Arcanineb, (240,240))

    def Arcaninefront():
        Arcaninef = pygame.image.load("Images/arcanine.png")
        Arcaninef = pygame.transform.scale(Arcaninef, (240,240))

    def Rhydonfront():
        Rhydonf = pygame.image.load("Images/rhydon.png")
        Rhydonf = pygame.transform.scale(Rhydonf, (240,240))

    def Rhydonback():
        Rhydonb = pygame.image.load("Images/rhydonback.png")
        Rhydonb = pygame.transform.scale(Rhydonb, (240,240))

    def Blastoisefront():
        Blastoisef = pygame.image.load("Images/blastoise.png")
        Blastoisef = pygame.transform.scale(Blastoisef, (240,240))

    def Blastoiseback():
        Blastoiseb = pygame.image.load("Images/blastoiseback.png")
        Blastoiseb = pygame.transform.scale(Blastoiseb, (240,240))