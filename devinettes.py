import random

def jouer():

    nb_secret= random.randint(0,100)
    tentative=0
    maxTentative=10

    print("Bienvenue je pense à un nombre entre 0 et 100")
    print(f"Tu as {maxTentative} essais.\n")

    while tentative<maxTentative:
        saisie=input("Ton nombre : ")

        try:
            guess=int(saisie)
            tentative+=1
            if guess<nb_secret:
                print("Trop petit")
            elif guess>nb_secret:
                print("Trop grand")
            else:
                print(f"Bravo tu as trouvé le nombre secret secret {nb_secret} en {tentative} essais.")
                return
            print(f"Il te reste {maxTentative-tentative} essais\n")                          
        except ValueError:
            print("Tu dois saisir un nombre\n")
    print(f"Perdu ! Le nombre à deviner était {nb_secret}")  
    

jouer()