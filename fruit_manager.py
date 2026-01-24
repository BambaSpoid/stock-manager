import json


def ouvrir_inventaire(path="inventaires.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


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
