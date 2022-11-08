def add (x,y):
    return x+y
print(3,5)

def sub (x,y):
    return x-y
print(3,5)

def multiply (x,y):
    return x*y
print(3,5)

def divide (x,y):
    return x/y
print(3,5)

def modulo (x,y):
    return x%y
print(3,5)

def revenuSeconde(salaireHeure, heureJourOuvrable, jourOuvrable):
    return(jourOuvrable * heureJourOuvrable) * (salaireHeure)/365/24/60/60
print(revenuSeconde(2000,17,303))

def salaireNet(prc,salaireBrut):
    return salaireBrut - (prc/100 * salaireBrut)
print(salaireNet(25,2000))