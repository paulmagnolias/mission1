total = 0 
with open("depenses.txt") as fichier:
    for ligne in fichier:
        total = total + int(ligne)
print (total)