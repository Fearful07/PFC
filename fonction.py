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
