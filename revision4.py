depenses = {"resto": 12, "loyer": 150, "essence": 30}
total = 0
for categorie, montant in depenses.items():
    total = montant + total
print (total)