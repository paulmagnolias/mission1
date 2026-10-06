def meilleure_note(liste):
    meilleure = liste[0]
    for note in liste:
        if note > meilleure:
            meilleure = note
    return meilleure