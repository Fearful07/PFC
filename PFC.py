"""
DEBUT

On admet une fonction random qui renvoie un chiffre aléatoire entre un min et un max (random(min,max))
On ademet une fonction input qui recupere l'entree d'un joueur

Definir une fonction pierreFeuilleCiseau sans parametre
    Assigne à la variable bestOff le retour de l'execution de la fonction input avec en parametre le message("Voulez-vous faire un BO1, BO3 ou BO5")
    initialiser la variable scoreJoueur a 0
    initialiser la variable scoreBot a 0
    Tant que le scoreJoueur n'est pas égale à 2 et que le scoreBot n'est pas égale a 2
        Alors
        Assigne à la variable choixJoueur le retour de l'execution de la fonction input avec en parametre le message("Pierre, Feuille, Ciseau ? ")
        Tant que le choixJoueur n'est pas égale a "Pierre" n'est pas égale a "Feuille" n'est pas égale a "Ciseau"
            reappeler la fonction input("Rentrer le mot correct")
        definir une liste choice qui comprend Pierre, Feuille et Ciseau
        Assigne à la variable choixBot la correspondance du retour de l'execution de random avec comme parametre(0,2) dans la liste choixPossible
        si le choixJoueur est égale a pierre et le choixBot est égale a ciseau 
        ou le choixJoueur est égale a feuille et le choixBot est égale a pierre 
        ou le choixJoueur est égale a ciseau et le choixBot est égale a feuille
            alors
            on ajoute 1 a la variable scoreJoueur
            affiche Gagner le score est : avec le (scoreJoueur - le scoreBot)
        sinon si le choixJoueur est egal au choixBot
            alors 
            affiche égalité
        sinon
            alors
            on ajoute 1 a la variable scoreBot 
            affiche Perdu le score est : avec le (scoreJoueur - le scoreBot)
    si le scoreJoueur est 2
        alors afficher Victoire, Fin de la partie
    sinon
        afficher Défaite, Fin de la partie
            
    assigne a la variable restart le retour de l'execution de la fonction input avec en parametre le message("Voulez vous recommencer ? ")
    si le restart est égal a "oui"
        alors on réexécute la fonction pierreFeuilleCiseau()
FIN
"""



