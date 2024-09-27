taille_tableau = int(input("Entrez le nombre de personnes : "))

personnes = []

for i in range(taille_tableau):
    print(f"\nSaisie des informations pour la personne {i+1}:")
    
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    note = float(input("Entrez la note : "))
    moyenne = float(input("Entrez la moyenne : "))
    classe = input("Entrez la classe : ")
    
    personne = {
        "Prénom": prenom,
        "Nom": nom,
        "Note": note,
        "Moyenne": moyenne,
        "Classe": classe
    }
    
    personnes.append(personne)

# Affichage des résultats de la saisie
print("\nInformations des personnes saisies :")
for idx, personne in enumerate(personnes, 1):
    print(f"\nPersonne {idx}:")
    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")