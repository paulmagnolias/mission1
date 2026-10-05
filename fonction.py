def somme(liste):
    total = 0
    for nombre in liste:
        total = total + nombre
    return total

print(somme([15, 25, 40, 70]))
print(somme([1, 2, 3]))