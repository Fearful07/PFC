import random

def pierreFeuilleCiseau():
    choixJoueur = input("Pierre, Feuille, Ciseau ? ")
    while choixJoueur != "Pierre" and choixJoueur != "Feuille" and choixJoueur != "Ciseau":
        choixJoueur = input("Rentrer le mot correct")
    choice = ["Pierre", "Feuille", "Ciseau"]
    choixBot = choice[random.randint(0,2)]
    if (choixJoueur == "Pierre" and choixBot == "Ciseau") or (choixJoueur == "Feuille" and choixBot == "Pierre") or (choixJoueur == "Ciseau" and choixBot == "Feuille"):
        print("Victoire")  
    elif choixJoueur == choixBot:
        print("égalité")  
    else:
        print("Défaite")  
    restart = input("Voulez vous recommencer ? oui ou non ")
    if restart == "oui":
        pierreFeuilleCiseau()


print(pierreFeuilleCiseau())