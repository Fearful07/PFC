import random

def pierreFeuilleCiseau():
    bestOff = int(input("Le premier à combien ? "))
    print(bestOff)
    scoreJoueur = 0
    scoreBot = 0
    nbRound = 0
    while scoreJoueur != bestOff and scoreBot != bestOff:
        choixJoueur = input("Pierre, Feuille, Ciseau ? ")
        nbRound += 1
        while choixJoueur != "Pierre" and choixJoueur != "Feuille" and choixJoueur != "Ciseau":
            choixJoueur = input("Rentrer le mot correct ")
        choice = ["Pierre", "Feuille", "Ciseau"]
        choixBot = choice[random.randint(0,2)]
        if (choixJoueur == "Pierre" and choixBot == "Ciseau") or (choixJoueur == "Feuille" and choixBot == "Pierre") or (choixJoueur == "Ciseau" and choixBot == "Feuille"):
            scoreJoueur = scoreJoueur + 1
            print(f"Gagné le score est:  {scoreJoueur} - {scoreBot}")
        elif choixJoueur == choixBot:
            print("égalité")  
        else:
            scoreBot = scoreBot + 1
            print(f"Perdu le score est:  {scoreJoueur} - {scoreBot}")
    if scoreJoueur == bestOff:
        print("Victoire, Fin de la partie", "Avec", nbRound, "joué")
    else:
        print("Défaite, Fin de la partie", "Avec", nbRound, "round joué")

    restart = input("Voulez vous recommencer ? oui ou non ")
    if restart == "oui":
        pierreFeuilleCiseau()

print(pierreFeuilleCiseau())