from Pokemon import *
from Eau import *
from Feu import *
from Normal import *
from Terre import *

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
        if self.pokemon1.getPV() == 0 or self.pokemon2.getPV() == 0:
            self.partieFinie = True
            return self.partieFinie
        else:
            pass

    
    def affichageVainqueur(self):
        if self.pokemon1(self.getPV()) == 0:
            self.vainqueur = "Le vainqueur est {}".format(self.pokemon2.getNom()) 
            return self.vainqueur
        elif self.pokemon2(self.getPV()) == 0:
            self.vainqueur = "Le vainqueur est {}".format(self.pokemon1.getNom())
            return self.vainqueur
    
    
    def affichagePerdant(self):
        if self.pokemon1(self.getPV()) == 0:
            self.perdant = "Le perdant est {}".format(self.pokemon1.getNom())
            return self.perdant
        elif self.pokemon2(self.getPV()) == 0:
            self.perdant = "Le perdant est {}".format(self.pokemon2.getNom())
            return self.perdant
    
    
    def typeEtPuissancePokemon1(self):
        if self.pokemon1.puissanceAttaque == 90:
            self.pokemon1.type = "Terre"
            return self.pokemon1.type
        elif self.pokemon1.puissanceAttaque == 100:
            self.pokemon1.type = "Normal"
            return self.pokemon1.type
        elif self.pokemon1.puissanceAttaque == 150:
            self.pokemon1.type = "Feu"
            return self.pokemon1.type
        elif self.pokemon1.puissanceAttaque == 220:
            self.pokemon1.type = "Eau"
            return self.pokemon1.type
    
    
    def typeEtPuissancePokemon2(self):
        if self.pokemon2.puissanceAttaque == 90:
            self.pokemon2.type = "Terre"
            return self.pokemon2.type
        elif self.pokemon2.puissanceAttaque == 100:
            self.pokemon2.type = "Normal"
            return self.pokemon2.type
        elif self.pokemon2.puissanceAttaque == 150:
            self.pokemon2.type = "Feu"
            return self.pokemon2.type
        elif self.pokemon2.puissanceAttaque == 220:
            self.pokemon2.type = "Eau"
            return self.pokemon2.type
    
    
    
    def tableDesTypes(self):
        if self.pokemon1.type == "Feu" and self.pokemon2.type == "Eau":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.5
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 2 
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Feu" and self.pokemon2.type == "Terre":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 2
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Eau" and self.pokemon2.type == "Feu":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 2
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Eau" and self.pokemon2.type == "Terre":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.5
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Terre" and self.pokemon2.type == "Eau":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 2
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Terre" and self.pokemon2.type == "Feu":
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.5
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon1.type == "Normal" and (self.pokemon2.type == "Terre" or self.pokemon2.type == "Feu" or self.pokemon2.type == "Eau"):
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.75
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 1
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Feu" and self.pokemon1.type == "Eau":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.5
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 2 
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Feu" and self.pokemon1.type == "Terre":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 2
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Eau" and self.pokemon1.type == "Feu":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 2
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.5
            return self.pokemon2.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Eau" and self.pokemon1.type == "Terre":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.5
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Terre" and self.pokemon1.type == "Eau":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 2
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 0.5
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Terre" and self.pokemon1.type == "Feu":
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.5
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 2
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
        elif self.pokemon2.type == "Normal" and (self.pokemon1.type == "Terre" or self.pokemon1.type == "Feu" or self.pokemon1.type == "Eau"):
            self.pokemon2.puissanceAttaque = self.pokemon2.puissance * 0.75
            self.pokemon1.puissanceAttaque = self.pokemon1.puissance * 1
            return self.pokemon1.puissanceAttaque, self.pokemon2.puissanceAttaque
    
    
    
    def degatsPV(self):
        while self.partieFinie == False:
            if self.rounds%2 != 0:
                self.pokemon2.setPV(self.pokemon2.getPV() - (self.pokemon1.puissanceAttaque - self.pokemon2.defense))
                self.rounds += 1
                self.pokemonKO()
            elif self.rounds%2 == 0:
                self.pokemon1.setPV(self.pokemon1.getPV() - (self.pokemon2.puissanceAttaque - self.pokemon1.defense))
                self.rounds += 1 
                self.pokemonKO()


Ronflex = typeNormal("Ronflex", 50)
Ronflex.affichageTypeNormal()
Tortank = typeEau("Tortank", 50)
Tortank.affichageTypeEau()
Arcanin = typeFeu("Arcanin", 50)
Arcanin.affichageTypeFeu()
Onyx = typeTerre("Onyx", 50)
Onyx.affichageTypeTerre()

