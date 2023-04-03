from Combat import *



print("Menu:")
print("\n")
print("1. Lancer la partie")


choice = int(input())

#Il y a quatres pokémons disponibles : Ronflex, Rhinoféros, Tortank et Arcanin
#On peut les remplacer dans le choice

if choice == 1:
    combat1 = Combat()
    #En dessous on peut remplacer les pokémons par ceux disponibles écrit au dessus.
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
else:
    print("Erreur")