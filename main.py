age = int(input("Quel est ton âge ? "))
budget = int(input("Quel est ton budget (en euros) ? "))

if age < 18 or budget < 20:
    print("Recommandation : une sortie au parc ou un cinéma.")
elif age >= 65 and budget >= 50:
    print("Recommandation : un concert classique ou un bon restaurant.")
elif budget >= 1000:
    print("Recommandation : un voyage.")
elif age >= 18 and age <= 30 and budget >= 200 and budget <= 999:
    print("Recommandation : un festival.")
elif age >= 18 and budget >= 100:
    print("Recommandation : un week-end ou une expérience premium.")
elif  age >= 18:
    print("Recommandation : un cinéma ou un resto sympa.")
else:
    print("Recommandation : un cinéma ou un resto sympa.")
