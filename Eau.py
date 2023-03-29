from Pokemon import *

class typeEau(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau)
        self.setPV(120)
        self.puissanceAttaque = 220
        self.defense = 60
    def affichageTypeEau(self):
        print("Le nom du Pokémon est", self.getNom())
        print("{} possède {} points de vie".format((self.getNom()),self.getPV()))
        print("{} possède {} points d'attaque".format(self.getNom(), self.puissanceAttaque))
        print("{} possède {} points de défense".format(self.getNom(), self.defense))
        
Leviator = typeEau("Leviator", 50)
Leviator.affichageTypeEau()