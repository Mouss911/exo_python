print("Calculatrice")
while True:
    print("\n1. Faire la somme de deux valeurs")
    print("2. Faire la soustraction de deux valeurs")
    print("3. Faire le produit de deux valeurs")
    print("4. Faire la division de deux valeurs")
    print("5. Quitter")
    choix = input("Choisissez une option : ")
    if choix == "5":
        break
    elif choix in ["1", "2", "3", "4"]:
        valeur1 = float(input("Entrez la première valeur : "))
        valeur2 = float(input("Entrez la deuxième valeur : "))
        if choix == "1":
            print(f"La somme de {valeur1} et {valeur2} est {valeur1 + valeur2}")
        elif choix == "2":
            print(f"La soustraction de {valeur1} et {valeur2} est {valeur1 - valeur2}")
        elif choix == "3":
            print(f"Le produit de {valeur1} et {valeur2} est {valeur1 * valeur2}")
        elif choix == "4":
            if valeur2 != 0:
                print(f"La division de {valeur1} et {valeur2} est {valeur1 / valeur2}")
            else:
                print("Erreur : Division par zéro")
    else:
        print("Erreur : Choix invalide")