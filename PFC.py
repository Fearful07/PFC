"""
DEBUT

On admet une fonction random qui renvoie un chiffre aléatoire entre un min et un max (random(min,max))
On ademet une fonction input qui recupere l'entree d'un joueur

Definir une fonction pierreFeuilleCiseau sans parametre
    Assigne à la variable choixJoueur le retour de la fonction input("Pierre, Feuille, Ciseau ? ")
    Tant que le choixJoueur n'est pas egale a l'un des choix de la liste
        reappeler la fonction input("Rentrer le mot correct")
    definir une liste choice qui comprend Pierre, Feuille et Ciseau
    Assigne à la variable choixBot la correspondance du retour de random(0,2) dans la liste choixPossible
    si le choixJoueur est pierre et le choixBot est ciseau 
    ou le choixJoueur est feuille et le choixBot est pierre 
    ou le choixJoueur est ciseau et le choixBot est feuille
        alors
        affiche gagner
    sinon si le choixJoueur est egal au choixBot
        alors 
        affiche égalité
    sinon
        alors
        affiche perdu
    assigne a la variable restart le retour de input("Voulez vous recommencer ? ")
    si le restart est égal a oui
        alors
        on réexécute la fonction pierreFeuilleCiseau()
FIN
"""



