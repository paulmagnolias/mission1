def compter_majeurs(liste):
    compteur = 0
    for age in liste:
        if age >= 18:
            compteur = compteur + 1
    return compteur

print(compter_majeurs([15, 25, 40, 70]))