inventaires = {
    "bananes": 120,
    "mangues": 85,
    "ananas": 45,
    "noix de coco": 60,
    "papayes": 30,
}


def afficher_inventaire(inventaire):
    print("Inventaire des fruits :")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")


def recolter(inventaire, fruit, quantite):
    if fruit in inventaire:
        inventaire[fruit] += quantite
    else:
        inventaire[fruit] = quantite
    print(f"Récolté {quantite} {fruit} supplémentaires.")


def vendre(inventaire, fruit, quantite):
    if fruit in inventaire and inventaire[fruit] >= quantite:
        inventaire[fruit] -= quantite
        print(f"Vendu {quantite} {fruit}.")
    else:
        print(f"Stock insuffisant pour {fruit}.")


if __name__ == "__main__":
    afficher_inventaire(inventaires)
    recolter(inventaires, "mangues", 20)
    vendre(inventaires, "bananes", 50)
    afficher_inventaire(inventaires)
