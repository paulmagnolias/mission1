def grosse_depenses (depenses):
    RESULTAT = []
    for depense in depenses:
        if depense > 100:
            RESULTAT.append(depense)
    return RESULTAT

print(grosse_depenses([12, 150, 30, 200, 8]))