def meilleure_note (liste):
    meilleure = 0
    for note in liste:
        if note > meilleure:
            meilleure = note
    return meilleure

print (meilleure_note([12, 8, 4, 9]))