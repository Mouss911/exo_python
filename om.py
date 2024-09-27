def afficher_menu_principal():
    print("\n--- Menu Orange Money ---")
    print("1. Solde de mon compte")
    print("2. Transfert d’argent")
    print("3. Paiement de facture")
    print("4. Achats de crédit")
    print("5. Quitter")
    choix = input("Veuillez choisir une option : ")
    return choix

def afficher_solde():
    solde = 10000  # Solde par défaut
    print(f"Votre solde actuel est : {solde} F CFA.")

def transfert_argent():
    while True:
        print("\n--- Transfert d'argent ---")
        print("1. Saisir le montant à transférer")
        print("2. Quitter")
        choix = input("Veuillez choisir une option : ")
        
        if choix == "1":
            montant = input("Veuillez saisir le montant à transférer : ")
            print(f"Vous avez transféré {montant} F CFA.")
        elif choix == "2":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

def paiement_facture():
    while True:
        print("\n--- Paiement de facture ---")
        print("1. Liquide")
        print("2. Chèque")
        print("3. Quitter")
        choix = input("Veuillez choisir une option : ")
        
        if choix == "1":
            montant = int(input("Veuillez saisir le montant (entier) : "))
            print(f"Vous avez payé {montant} F CFA en liquide.")
        elif choix == "2":
            montant = input("Veuillez saisir le montant (chèque) : ")
            print(f"Vous avez payé {montant} F CFA par chèque.")
        elif choix == "3":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

def achat_credit():
    numero = input("\nVeuillez entrer le numéro de téléphone : ")
    montant = input("Veuillez entrer le montant du crédit : ")
    print(f"Vous avez acheté {montant} F CFA de crédit pour le numéro {numero}.")

def main():
    while True:
        choix = afficher_menu_principal()
        
        if choix == "1":
            afficher_solde()
        elif choix == "2":
            transfert_argent()
        elif choix == "3":
            paiement_facture()
        elif choix == "4":
            achat_credit()
        elif choix == "5":
            print("Merci d'utiliser Orange Money. À bientôt !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Exécution du programme
if __name__ == "__main__":
    main()
