from Pokemon import *

class typeTerre(Pokemon):
    
    
    def __init__(self, nom, niveau, pv, atq, defen):
        Pokemon.__init__(self)
        self.setNom(nom)
        self.niveau = niveau
        self.setPV(pv)
        self.puissanceAttaque = atq
        self.defense = defen
    
    
    def affichageType(self):
        print("\n")
        print("Le nom du Pokémon est", self.getNom())
        print("{} possède {} points de vie".format((self.getNom()),self.getPV()))
        print("{} possède {} points d'attaque".format(self.getNom(), self.puissanceAttaque))
        print("{} possède {} points de défense".format(self.getNom(), self.defense))
        print("\n")
        

