import random

def creer_dico_scrabble():
    return {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }

def score_scrabble(mot, dico):
    return sum(dico[lettre.upper()] for lettre in mot if lettre.upper() in dico)

eleves = {
    "Léa": ["Maths", "Physique", "Informatique"],
    "Lucas": ["SVT", "Chimie", "Philosophie"]
}

def ajouter_eleve(nom, specialites):
    eleves[nom] = specialites

def supprimer_premier_eleve():
    eleves.pop(next(iter(eleves)))

def modifier_specialite(nom, ancienne, nouvelle):
    if nom in eleves and ancienne in eleves[nom]:
        eleves[nom][eleves[nom].index(ancienne)] = nouvelle

def afficher_specialites(nom):
    return eleves.get(nom, "Élève non trouvé")

def generer_cle_chiffrement():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    melange = alphabet[:]
    random.shuffle(melange)
    return dict(zip(alphabet, melange))

def chiffrer(mot, cle):
    return "".join(cle.get(lettre.upper(), lettre) for lettre in mot)

def dechiffrer(mot, cle):
    inverse_cle = {v: k for k, v in cle.items()}
    return "".join(inverse_cle.get(lettre.upper(), lettre) for lettre in mot)

Terminale = {}

def creerEleve(base, identifiant):
    base[identifiant] = {
        "nom": input("Nom: "),
        "prénom": input("Prénom: "),
        "âge": input("Âge: "),
        "notes": {}
    }

def supprimerEleve(base, identifiant):
    base.pop(identifiant, None)

def afficherMatiere(base, identifiant):
    return list(base.get(identifiant, {}).get("notes", {}).keys())

def ajouterMatiere(base, identifiant, matiere):
    if identifiant in base:
        base[identifiant]["notes"][matiere] = []
        while (note := input("Ajouter une note (vide pour arrêter): ")):
            base[identifiant]["notes"][matiere].append(float(note))

def supprimerMatiere(base, identifiant, matiere):
    base.get(identifiant, {}).get("notes", {}).pop(matiere, None)

def calculerMoyenne(notes):
    return sum(notes) / len(notes) if notes else 0

def afficherProfil(base, identifiant):
    eleve = base.get(identifiant)
    if not eleve:
        return "Élève non trouvé"
    profil = f"ID: {identifiant}, Nom: {eleve['nom']}, Prénom: {eleve['prénom']}, Âge: {eleve['âge']}\n"
    for matiere, notes in eleve["notes"].items():
        profil += f"{matiere}: Moyenne {calculerMoyenne(notes):.2f}\n"
    return profil

def menu():
    while True:
        choix = input("1. Ajouter élève\n2. Supprimer élève\n3. Afficher matières\n4. Ajouter matière\n5. Supprimer matière\n6. Afficher profil\n7. Quitter\n")
        if choix == "1":
            creerEleve(Terminale, input("ID de l'élève: "))
        elif choix == "2":
            supprimerEleve(Terminale, input("ID de l'élève: "))
        elif choix == "3":
            print(afficherMatiere(Terminale, input("ID de l'élève: ")))
        elif choix == "4":
            ajouterMatiere(Terminale, input("ID: "), input("Matière: "))
        elif choix == "5":
            supprimerMatiere(Terminale, input("ID: "), input("Matière: "))
        elif choix == "6":
            print(afficherProfil(Terminale, input("ID: ")))
        elif choix == "7":
            break
