from Pokemon import *
from Eau import *
from Feu import *
from Normal import *
from Terre import *
from time import *
import time

class Combat(Pokemon):
    
    def valeursCombat(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.vainqueur = ""
        self.perdant = ""
        self.partieFinie = False
        self.pokemon1.type = ""
        self.pokemon2.type = ""
        self.rounds = 1

    def pokemonKO(self):
        if self.pokemon1.getPV() <= 0 or self.pokemon2.getPV() <= 0:
            self.partieFinie = True
            return self.partieFinie
        else:
            pass

    
    def choixVainqueur(self):
        if self.pokemon1.getPV() <= 0:
            self.vainqueur = "Le vainqueur est {}".format(self.pokemon2.getNom()) 
            return self.vainqueur
        elif self.pokemon2.getPV() <= 0:
            self.vainqueur = "Le vainqueur est {}".format(self.pokemon1.getNom())
            return self.vainqueur
    
    
    def choixPerdant(self):
        if self.pokemon1.getPV() <= 0:
            self.perdant = "Le perdant est {}".format(self.pokemon1.getNom())
            return self.perdant
        elif self.pokemon2.getPV() <= 0:
            self.perdant = "Le perdant est {}".format(self.pokemon2.getNom())
            return self.perdant
        
    def affichageVainqueur(self):
        print(self.vainqueur)

    def affichagePerdant(self):
        print(self.perdant)
    
    
    def typeEtPuissancePokemon1(self):
        if self.pokemon1.getNom() == "Rhinoféros":
            self.pokemon1.type = "Terre"
            return self.pokemon1.type
        elif self.pokemon1.getNom() == "Ronflex":
            self.pokemon1.type = "Normal"
            return self.pokemon1.type
        elif self.pokemon1.getNom() == "Arcanin":
            self.pokemon1.type = "Feu"
            return self.pokemon1.type
        elif self.pokemon1.getNom() == "Tortank":
            self.pokemon1.type = "Eau"
            return self.pokemon1.type
    
    
    def typeEtPuissancePokemon2(self):
        if self.pokemon2.getNom() == "Rhinoféros":
            self.pokemon2.type = "Terre"
            return self.pokemon2.type
        elif self.pokemon2.getNom() == "Ronflex":
            self.pokemon2.type = "Normal"
            return self.pokemon2.type
        elif self.pokemon2.getNom() == "Arcanin":
            self.pokemon2.type = "Feu"
            return self.pokemon2.type
        elif self.pokemon2.getNom() == "Tortank":
            self.pokemon2.type = "Eau"
            return self.pokemon2.type
    
    
    
    def tableDesTypes(self):
        if self.pokemon1.type == "Feu" and self.pokemon2.type == "Eau":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.5
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 2 
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Feu" and self.pokemon2.type == "Terre":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 2
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Eau" and self.pokemon2.type == "Feu":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 2
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Eau" and self.pokemon2.type == "Terre":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.5
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Terre" and self.pokemon2.type == "Eau":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 2
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Terre" and self.pokemon2.type == "Feu":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.5
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Normal" and (self.pokemon2.type == "Terre" or self.pokemon2.type == "Feu" or self.pokemon2.type == "Eau"):
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.75
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 1
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Feu" and self.pokemon1.type == "Eau":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.5
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 2 
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Feu" and self.pokemon1.type == "Terre":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 2
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Eau" and self.pokemon1.type == "Feu":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 2
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.5
            return self.pokemon2.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Eau" and self.pokemon1.type == "Terre":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.5
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Terre" and self.pokemon1.type == "Eau":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 2
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Terre" and self.pokemon1.type == "Feu":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.5
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Normal" and (self.pokemon1.type == "Terre" or self.pokemon1.type == "Feu" or self.pokemon1.type == "Eau"):
            self.pokemon2.puissanceAttaque = self.pokemon2.puissanceAttaque * 0.75
            self.pokemon1.puissanceAttaque = self.pokemon1.puissanceAttaque * 1
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        
    def affichageStatsPokemon1(self):
        print("\n")
        print("Le nom du premier Pokémon est {} de type {}".format(self.pokemon1.getNom(), self.pokemon1.type))
        print("{} possède {} points de vie".format((self.pokemon1.getNom()),self.pokemon1.getPV()))
        print("{} possède {} points d'attaque".format(self.pokemon1.getNom(), self.pokemon1.puissanceAttaque))
        print("{} possède {} points de défense".format(self.pokemon1.getNom(), self.pokemon1.defense))
        print("\n")

    def affichageStatsPokemon2(self):
        print("\n")
        print("Le nom du deuxième Pokémon est {} de type {}".format(self.pokemon2.getNom(), self.pokemon2.type))
        print("{} possède {} points de vie".format((self.pokemon2.getNom()),self.pokemon2.getPV()))
        print("{} possède {} points d'attaque".format(self.pokemon2.getNom(), self.pokemon2.puissanceAttaque))
        print("{} possède {} points de défense".format(self.pokemon2.getNom(), self.pokemon2.defense))
        print("\n")
    
    
    
    def degatsPV(self):
        while self.partieFinie == False:
            if self.rounds%2 != 0:
                self.pokemon2.setPV(self.pokemon2.getPV() - ((self.pokemon1.puissanceAttaque) - (self.pokemon2.defense * 0.25)))
                self.rounds += 1
                if self.pokemon2.getPV() > 0:
                    print("{} a attaqué {}, {} a {} points de vie restants".format(self.pokemon1.getNom(), self.pokemon2.getNom(), self.pokemon2.getNom(), self.pokemon2.getPV()))
                    print("\n")
                elif self.pokemon2.getPV() <= 0:
                    print("{} a attaqué {}, {} n'a plus de points de vie restants, il est K.O.".format(self.pokemon1.getNom(), self.pokemon2.getNom(), self.pokemon2.getNom()))
                    print("\n")
                    self.pokemonKO()
            elif self.rounds%2 == 0:
                self.pokemon1.setPV(self.pokemon1.getPV() - ((self.pokemon2.puissanceAttaque) - (self.pokemon1.defense * 0.25)))
                self.rounds += 1 
                if self.pokemon1.getPV() > 0:
                    print("{} a attaqué {}, {} a {} points de vie restants".format(self.pokemon2.getNom(), self.pokemon1.getNom(), self.pokemon1.getNom(), self.pokemon1.getPV()))
                    print("\n")
                elif self.pokemon1.getPV() <= 0:
                    print("{} a attaqué {}, {} n'a plus de points de vie restants, il est K.O.".format(self.pokemon2.getNom(), self.pokemon1.getNom(), self.pokemon1.getNom()))
                    print("\n")
                    self.pokemonKO()
            time.sleep(1)

Ronflex = typeNormal("Ronflex", 100, 461,256,166)

Tortank = typeEau("Tortank", 100, 299, 202, 236)

Arcanin = typeFeu("Arcanin", 100, 321, 256, 196)

Rhinoféros = typeTerre("Rhinoféros", 100, 351,296,276)


combat1 = Combat()
combat1.valeursCombat(Ronflex, Rhinoféros)
combat1.typeEtPuissancePokemon1()
combat1.typeEtPuissancePokemon2()
combat1.tableDesTypes()
combat1.affichageStatsPokemon1()
combat1.affichageStatsPokemon2()
combat1.degatsPV()
combat1.choixPerdant()
combat1.choixVainqueur()
combat1.affichageVainqueur()
combat1.affichagePerdant()