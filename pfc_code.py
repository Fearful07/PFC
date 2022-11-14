# DEBUT
import random
# On admet une fonction random qui renvoie un chiffre aléatoire entre un min et un max (random(min,max))
# On ademet une fonction input qui recupere l'entree d'un joueur

# Definir une fonction pierreFeuilleCiseau sans parametre
def pierreFeuilleCiseau():
#     Assigne à la variable bestOff le retour de l'execution de la fonction input avec en parametre le message("Le premier à combien ? ") transformer en integer
    bestOff = int(input("Le premier à combien ? "))
#     initialiser la variable scoreJoueur a 0
    scoreJoueur = 0
#     initialiser la variable scoreBot a 0
    scoreBot = 0
#     initialiser la variable nbRound a 0
    nbRound = 0
#     Tant que le scoreJoueur n'est pas égale à bestOff et que le scoreBot n'est pas égale à bestOff
    while scoreJoueur != bestOff and scoreBot != bestOff:
#         Alors
#         Assigne à la variable choixJoueur le retour de l'execution de la fonction input avec en parametre le message("Pierre, Feuille, Ciseau ? ")
        choixJoueur = input("Pierre, Feuille, Ciseau ? ")
#         et ajouter 1 a la variable nbRound
        nbRound = nbRound + 1
#         Tant que le choixJoueur n'est pas égale a "Pierre" et n'est pas égale a "Feuille" et n'est pas égale a "Ciseau"
        while choixJoueur != "Pierre" and choixJoueur != "Feuille" and choixJoueur != "Ciseau":
#             reappeler la fonction input("Rentrer le mot correct")
            input("Rentrer le mot correct")
#         assigne a la variable une liste choice qui comprend Pierre, Feuille et Ciseau
        choice = ["Pierre", "Feuille", "Ciseau"]
#         Assigne à la variable choixBot la correspondance du retour de l'execution de random avec comme parametre(0,2) dans la liste choice
        choixBot = random.randint(choice(0,2)
#         Si le choixJoueur est égale a pierre et le choixBot est égale a ciseau
#         ou le choixJoueur est égale a feuille et le choixBot est égale a pierre 
#         ou le choixJoueur est égale a ciseau et le choixBot est égale a feuille
#             alors
#             on ajoute 1 a la variable scoreJoueur
#             affiche Gagner le score est : avec le (scoreJoueur - le scoreBot)
#         Sinon si le choixJoueur est egal au choixBot
#             alors 
#             affiche égalité
#         Sinon
#             alors
#             on ajoute 1 a la variable scoreBot 
#             affiche Perdu le score est : avec le (scoreJoueur - le scoreBot)
#     Si le scoreJoueur est égale a la variable bestOff
#         alors afficher Victoire, Fin de la partie et la variable nbRound
#     Sinon
#         afficher Défaite, Fin de la partie et la variable nbRound
            
#     assigne a la variable restart le retour de l'execution de la fonction input avec en parametre le message("Voulez vous recommencer ? ")
#     si le restart est égal a "oui"
#         alors on réexécute la fonction pierreFeuilleCiseau()

# Execution de la fonction pierreFeuilleCiseau()       
# FIN




