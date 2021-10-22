#Feature à convertir pour être utilisable avec un bot

tableauSaisie=[]
tableauLettre=[]
tableauCrypto=[]
toto=[]
titi=[]
tata=[]
tab=[]

def saisieTableauLettre(tab):
    """initialisation tableau lettre"""
    for i in range (65,91):
        z=chr(i)
        tab.append(z)
    return tab

#Creation du tableau de reference
saisieTableauLettre(tableauLettre)

def saisieTableauCrypto(tableauCrypto):
    """initialisation tableau lettre crypto"""
    for i in range (66,91):
      c=chr(i)
      tableauCrypto.append(c)
    tableauCrypto.insert(25,"A") 
    return tableauCrypto 

#Creation du tableau crypte
saisieTableauCrypto(tableauCrypto)

def saisieTableauSaisie(tab):
    """saisie du tableau de depart """
    for i in range (taille):
        x=str(input("Saisir la lettre à ajouter dans le tableau : "))
        tab.append(x)
    return tab

def Crypt(tab):
     """changement de lettre Cryptage"""
     for i in range(0, taille):
        for j in range(0, 26):
            if tableauSaisie[i] == tableauLettre[j]:
                l=tableauCrypto[j]
                tab.append(l)
                j = 26
     return tab
    
def Decrypt(tab):
     """changement de lettre Decryptage """
     for i in range(0, taille):
        for j in range(0, 26):
            if toto[i] == tableauCrypto[j]:
                m=tableauLettre[j]
                tab.append(m)
                j = 26
     return tab
     
def Decrypt2(tab):
     """changement de lettre Decryptage """
     for i in range(0, taille):
        for j in range(0, 26):
            if tableauSaisie[i]  == tableauCrypto[j]:
                m=tableauLettre[j]
                tab.append(m)
                j = 26
     return tab
#affichage final

#programme principal

#nombre de lettre du mot à saisir
taille=int(input("Entrer le nombre de lettre à saisir : "))
#Mise en memoire du tableau saisie
tableauSaisie = saisieTableauSaisie(tableauSaisie)

Crypt=Crypt(toto)

rep=str(input("veuillez saisir votre choix \n C pour Crypter \n D pour decrypter la saisie crypter \n DD pour decrypter seulement \n"))

if (rep=='C'):
    print("le message ",tableauSaisie, "saisie devient crypté en ",Crypt)
elif (rep=='D'):
    print("le message encrypté de ", Crypt, "donne ",Decrypt(titi))
else :
    print("le message ",tableauSaisie, "saisie devient décrypté en ",Decrypt2(tata))

while True:
    # main program
    while True:
        answer = str(input('Run again? (y4/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Goodbye")
        break