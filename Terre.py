from Pokemon import *

class typeTerre(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau)
        self.setPV(200)
        self.puissanceAttaque = 50
        self.defense = 150
    def affichageTypeTerre(self):
        print("Le nom du Pokémon est", self.getNom())
        print("{} possède {} points de vie".format((self.getNom()),self.getPV()))
        print("{} possède {} points d'attaque".format(self.getNom(), self.puissanceAttaque))
        print("{} possède {} points de défense".format(self.getNom(), self.defense))
        
Onyx = typeTerre("Onyx", 50)
Onyx.affichageTypeTerre()
