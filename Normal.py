from Pokemon import *

class typeNormal(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau)
        self.setPV(180)
        self.puissanceAttaque = 100
        self.defense = 120
    def affichageTypeNormal(self):
        print("Le nom du Pokémon est", self.getNom())
        print("{} possède {} points de vie".format((self.getNom()),self.getPV()))
        print("{} possède {} points d'attaque".format(self.getNom(), self.puissanceAttaque))
        print("{} possède {} points de défense".format(self.getNom(), self.defense))
        
Ronflex = typeNormal("Ronflex", 50)
Ronflex.affichageTypeNormal()