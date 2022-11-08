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
    return x/y
print(divide(3,5))

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
    pourcent = prc/100 #mise en pourcentage 
    return salaireBrut - (pourcent * salaireBrut)
print(salaireNet(25,2000))