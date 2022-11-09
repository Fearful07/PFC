# #------------------Exercice 1-------------------
# def add (x,y):
#     return x+y
# print(add(3,5))

# def sub (x,y):
#     return x-y
# print(sub(3,5))

# def multiply (x,y):
#     return x*y
# print(multiply(3,5))

# def divide (x,y):
#     #si y == 0
#     if y == 0:
#         #alors on afficher le message pas possible
#         print("Il faut un y superieur à 0")
#         #et renvoyer rien
#         return
#     #Sinon on retourne x/y
#     return x/y

# print(divide(3,0))

# def modulo (x,y):
#     return x%y
# print(modulo(3,5))

# #------------------Exercice 2-------------------

# def revenuSeconde(salaireHeure, heureJourOuvrable, jourOuvrable):
#     # je calcul le salaire annuel
#     salairAnnuel = salaireHeure * heureJourOuvrable * jourOuvrable
#     # je calcul le nombre de seconde par An
#     nbSecondeParAn = 365 * 24 * 60 *60
#     # Je divise mon salaire par le nombre de secondes dans une année
#     return salairAnnuel / nbSecondeParAn
#     #return(jourOuvrable * heureJourOuvrable * salaireHeure) / (365*24*60*60)
# print(revenuSeconde(2000,17,303))

# def salaireNet(prc,salaireBrut):
#     #mise en pourcentage
#     percent = prc/100
#     # calcul de la reduction à appliqué
#     redu = percent*salaireBrut
#     # on soustrait le salaire brut au salaire
#     return salaireBrut - redu
# print(salaireNet(23,2000))

# def withdrawFees(total, percent):
#     #calcul du montant des taxes a retirer
#     fees = total * (percent / 100)
#     # Je retourne mon total sans les taxes
#     return total - fees

# #------------------Exercice 2: Les conditions si sinon, sinon si-------------------

# def calculSalaireNet(salaireBrut, public):
#     #Si j'occupe un poste de la fonction publique
#     if public:
#     #Alors je retourne le salaire brut - 15% de taxes
#         return withdrawFees(salaireBrut,15)
#     #Sinon c'est que je suis un travailleur privé,
#     else:
#     #Alors je retourne le salaire brut - 23% de douille bien a l'ancienne
#         return withdrawFees(salaireBrut,23)

# print(calculSalaireNet(2000,True))

# nbPersonne = x

# if nbPersonne == 1:
#     tuRentre()
# elif nbPersonne == 3:
#     tuRentre()
# elif nbPersonne == 5:
#     tuRentre()
# else:
#     tuRentrePas()

# #------------------Exercice 3 : Les BOUCLES-------------------
# tour = 0
# # Tant que je ne suis pas au tour 5
# while tour != 5 :
# # Appeler la fonction JouerUnTour
#     JouerUnTour()
# # J'effectue l'action de passer un tour
#     tour = tour + 1

#def input():
    #Renvoie un caractere de type string au hasard
#Exercice:
    #faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere
    #le caractere doit etre parametrable

#def bonCaractere(caractere):
    #on recupere un caractere aleatoire
    #inputCara = input()
    # compararer caractere avec inputCara
    #si les caractere sont les meme 
    # print victoire
    #et return rien
    #sinon 
    # tant que c'est perdu recommencer

#def bonCaractere(caractere):
    # On recupere un caractere aleatoire
    #inputCara = input()
    #tant que nos deux caractere ne sont pas égale
    # while inputCara != caractere 
        # Nouveau caractere importé
        # inputCara = input()
    #print("réussi")


#def
#  bonCaractere(caractere, nombreEssais=0):
    #inputCara = input()
    #if inputCara != caractere:
        #return bonCaractere(caractere,nombreEssais+1)
    #print("victoire")
    #return

# tab = [0,10,15,5,14,7,6,3,4,8,4,9,5,1,7,5,2,1,8,4,4,6,8]
# i = 0
# #Pour recuperer 15 je prend dans tableau l'index 3 - 1
# print(tab[2])

# len(tab) #Renvoie la longueur de tableau

# prenom = "Johann"
# nom = "Bois"

# nomPrenom = nom + prenom #renvoie BoisJohann
# nomPrenom = nom + " " + prenom #renvoie Bois Johann
# integerValue = 342
# strinInterValue = str(342) #Renvoie "342" au lieu de 342
# #Exercice
# #Faire une fonction qui concatene 2 chaine de caractere, les séparants par une virgule
# def concatene(mot1,mot2):
#     return mot1 + ", " + mot2
# print(concatene("Bois","Johann"))

# #Exercice 2
# #Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
# #avec l'ensemble des occuration d'un chiffre e.g.:
# tableau = [0,1,1,1,0,1,1,0,1]
# #la fonction(tableau,0) doit renvoyer "0 , 4, 7"

# def index(tableau,chiffre):
#     #on crée une variable de type string vide
#     index = ""
#     #on parcours les index de tous le tableau
#     for i in range(len(tableau)):
#         # si le chiffre du tableau est égale a notre chiffre
#         if tableau[i] == chiffre:
#             # si la variable est toujours vide 
#             if index == "":
#                 #on met comme premier valeur l'index de notre premier chiffre pour éviter un blanc
#                 index = str(i)
#             #sinon
#             else:
#                 #on ajouter a index tous les index qui corresponde grace a la fonction concatene crée au dessus
#                 index = concatene(index, str(i))
#     return index
# print(index(tableau,0))

# tableauCleVal = {"Cle" : "Valeur"}
# tableauCleVal["Cle"] # Renvoie "valeur"

# # foreach key: valeur in tableauCleVal
# #     print(key) #Renvoie "Cle"
# #     print(valeur) #Renvoie "Valeur"

# #Exercice 3 
# #faire une foction afficher un message
# def afficher(text):
#     print(text)
# afficher("aaaa")

# listeUtilisateur = {
#     "Johann" : "motdepasse",
#     "Michel" : "password",
#     "Toto" : "12345",
#     "JhonDoe" : "azerty"
# }
# #Ecrivez la fonction login(userName, password, listUser) permettant d'afficher un message de connexion si le combo user/password est bon

# def login(userName, password, listUser):
#     for i in listUser:
#         if userName == i and password == listUser[i]:
#             print("Vous êtes connecté")   
#             return 
#     print("Erreur, veuillez réessayer")
# login("Johann","motdepasse", listeUtilisateur)


# def fibonacci(xdebut,lenMax):
#     pour chaque valeur jusqu'à lenMax
#     for i in range(lenMax):
          #Si on es a la premiere valeur
#         if i == 0:
              #alors suite commence par 0
#             suite = "0"
          #Sinon si on es a la deuxieme valeur
#         elif i == 1:
              #alors on ecrit la valeur de xDebut dans la variable de fin
#             suite = concatene(suite, str(xdebut))
              # je stock ma premiere valeur
#             stock = 0
#         else:
              #j'aditionne les deux derniere valeur et les met dans une variable
#             xdebut = xdebut + stock
              #je la valeur precedente 
#             stock = xdebut - stock
              #on ecrit la valeur qui se trouve dans xdebut a la fin 
#             suite = concatene(suite, str(xdebut))
      #je retourne le resultat
#     return suite
# print(fibonacci(1,15))  
import random


def tab2Dim(lenTab):
    tab=[]
    for i in range(lenTab):
        tab.append([])
    for i in range(lenTab):
        for j in range(lenTab):
            tab[j].append(random.randint(0,10))
    return tab    
print(tab2Dim(5))

def adjacent(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i == 0 and j == 0:
                if 