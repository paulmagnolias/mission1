with open("depenses.txt") as fichier:
    for ligne in fichier:
        morceaux = ligne.strip() .split(",")
        print(morceaux[0], morceaux[1])