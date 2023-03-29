from Pokemon import *

class typeFeu(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau)
        self.setPV(150)
        self.puissanceAttaque = 150
        self.defense = 100
    def affichageTypeFeu(self):
        print("Le nom du Pokémon est", self.getNom())
        print("{} possède {} points de vie".format((self.getNom()),self.getPV()))
        print("{} possède {} points d'attaque".format(self.getNom(), self.puissanceAttaque))
        print("{} possède {} points de défense".format(self.getNom(), self.defense))
        
Maganon = typeFeu("Maganon", 50)
Maganon.affichageTypeFeu()