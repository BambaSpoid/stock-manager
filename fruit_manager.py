import json


def ouvrir_prix(path="data/prix.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def ouvrir_inventaire(path="data/inventaires.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def ecrire_inventaire(inventaire, path="data/inventaires.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(inventaire, f, ensure_ascii=False, indent=4)


def ouvrir_tresor(path="data/tresorie.txt"):
    with open(path, "r", encoding="utf-8") as f:
        tresorie = json.load(f)
    return tresorie


def ecrire_tresorerie(tresorie, path="data/tresorie.txt"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tresorie, f, ensure_ascii=False, indent=4)


def afficher_tresorerie(tresorie):
    print(f"Trésorerie actuelle : {tresorie:.2f} $")


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


def vendre(inventaire, fruit, quantite, tresorie, prix):
    if fruit in inventaire and inventaire[fruit] >= quantite:
        inventaire[fruit] -= quantite
        tresorie += quantite * prix.get(fruit, 0)
        print(f"Vendu {quantite} {fruit}.")
        return (inventaire, tresorie)
    else:
        print(f"Stock insuffisant pour {fruit}.")


if __name__ == "__main__":
    inventaires = ouvrir_inventaire()
    tresorerie = ouvrir_tresor()
    prix = ouvrir_prix()
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaires)
    recolter(inventaires, "mangues", 20)
    inventaires, tresorerie = vendre(inventaires, "bananes", 5, tresorerie, prix)
    afficher_inventaire(inventaires)
    ecrire_inventaire(inventaires)
    ecrire_tresorerie(tresorerie)
