class Pokemon():
    
    def __init__(self, nom, niveau):
        self.__nom = nom
        self.__pV = 100
        self.niveau = niveau
        self.puissanceAttaque = 0
        self.defense = 0
    def getNom(self):
        return self.__nom
    def getPV(self):
        return self.__pV
    def setPV(self, newPV):
        self.__pV = newPV
        return self.__pV
        
