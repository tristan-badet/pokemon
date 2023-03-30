class Pokemon():
    
    def __init__(self):
        self.__nom = ""
        self.__pV = 100
        self.niveau = 0
        self.puissanceAttaque = 0
        self.defense = 0
    
    
    def getNom(self):
        return self.__nom
    
    def setNom(self, nom):
        self.__nom = nom
        return self.__nom
    
    
    def getPV(self):
        return self.__pV
    
    
    def setPV(self, newPV):
        self.__pV = newPV
        return self.__pV
