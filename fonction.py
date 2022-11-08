#------------------Exercice 1-------------------
def add (x,y):
    return x+y
print(add(3,5))

def sub (x,y):
    return x-y
print(sub(3,5))

def multiply (x,y):
    return x*y
print(multiply(3,5))

def divide (x,y):
    #si y == 0
    if y == 0:
        #alors on afficher le message pas possible
        print("Il faut un y superieur à 0")
        #et renvoyer rien
        return
    #Sinon on retourne x/y
    return x/y

print(divide(3,0))

def modulo (x,y):
    return x%y
print(modulo(3,5))

#------------------Exercice 2-------------------

def revenuSeconde(salaireHeure, heureJourOuvrable, jourOuvrable):
    # je calcul le salaire annuel
    salairAnnuel = salaireHeure * heureJourOuvrable * jourOuvrable
    # je calcul le nombre de seconde par An
    nbSecondeParAn = 365 * 24 * 60 *60
    # Je divise mon salaire par le nombre de secondes dans une année
    return salairAnnuel / nbSecondeParAn
    #return(jourOuvrable * heureJourOuvrable * salaireHeure) / (365*24*60*60)
print(revenuSeconde(2000,17,303))

def salaireNet(prc,salaireBrut):
    #mise en pourcentage
    percent = prc/100
    # calcul de la reduction à appliqué
    redu = percent*salaireBrut
    # on soustrait le salaire brut au salaire
    return salaireBrut - redu
print(salaireNet(23,2000))

def withdrawFees(total, percent):
    #calcul du montant des taxes a retirer
    fees = total * (percent / 100)
    # Je retourne mon total sans les taxes
    return total - fees

#------------------Exercice 2: Les conditions si sinon, sinon si-------------------

def calculSalaireNet(salaireBrut, public):
    #Si j'occupe un poste de la fonction publique
    if public:
    #Alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaireBrut,15)
    #Sinon c'est que je suis un travailleur privé,
    else:
    #Alors je retourne le salaire brut - 23% de douille bien a l'ancienne
        return withdrawFees(salaireBrut,23)

print(calculSalaireNet(2000,True))

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

tab = [0,10,15,5,14,7,6,3,4,8,4,9,5,1,7,5,2,1,8,4,4,6,8]
i = 0
#Pour recuperer 15 je prend dans tableau l'index 3 - 1
print(tab[2])

len(tab) #Renvoie la longueur de tableau

prenom = "Johann"
nom = "Bois"

nomPrenom = nom + prenom #renvoie BoisJohann
nomPrenom = nom + " " + prenom #renvoie Bois Johann
integerValue = 342
strinInterValue = str(342) #Renvoie "342" au lieu de 342
#Exercice
#Faire une fonction qui concatene 2 chaine de caractere, les séparants par une virgule
def concatene(mot1,mot2):
    return mot1 + ", " + mot2
print(concatene("Bois","Johann"))

#Exercice 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensemble des occuration d'un chiffre e.g.:
tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0 , 4, 7"

def index(tableau,chiffre):
    index = ""
    for i in range(len(tableau)):
        if tableau[i] == chiffre:
            if index == "":
                index = str(i)
            else:
                index = concatene(index, str(i))
    return index
print(index(tableau,0))

