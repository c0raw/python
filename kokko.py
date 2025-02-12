gestionnaire = {
    'TFerragu': {
        'nom': 'Ferragu',
        'prenom': 'Thomas',
        'age': 25,
        'notes': {
            'Maths': [12, 14],
            'NSI': [14, 17, 15],
            'Physique': [20, 20]
        }
    },
    'BLéa': {
        'nom': 'Léa',
        'prenom': 'BARBERON',
        'age': 25,
        'notes': {
            'Maths': [20, 14],
            'NSI': [20, 14, 20, 20],
            'Physique': []
        }
    }
}

def getIdentifiant(nom: str, prenom: str) -> str:
    return prenom[0] + nom[:8]

def creerEleve(dico: dict):
    nom = input('Nom: ')
    prenom = input('Prénom: ')
    age = int(input('Âge: '))
    id = getIdentifiant(nom, prenom)
    dico[id] = {'nom': nom, 'prenom': prenom, 'age': age, 'notes': {}}
    print(f'Élève {id} ajouté.')

def supprimerEleve(dico: dict, id: str):
    if id in dico:
        del dico[id]
        print(f'Élève {id} supprimé.')
    else:
        print('Élève introuvable.')

def afficherMatiere(dico: dict, id: str):
    if id in dico:
        print(f'Matières de {id}: {list(dico[id]["notes"].keys())}')
    else:
        print('Élève introuvable.')

def ajouterMatiere(dico: dict, id: str):
    if id in dico:
        matiere = input('Nom de la matière: ')
        notes = list(map(int, input('Entrez les notes séparées par des espaces: ').split()))
        dico[id]['notes'][matiere] = notes
        print(f'Matière {matiere} ajoutée à {id}.')
    else:
        print('Élève introuvable.')

def supprimerMatiere(dico: dict, id: str, matiere: str):
    if id in dico and matiere in dico[id]['notes']:
        del dico[id]['notes'][matiere]
        print(f'Matière {matiere} supprimée pour {id}.')
    else:
        print('Élève ou matière introuvable.')

def calculerMoyenne(notes: list) -> float:
    return sum(notes) / len(notes) if notes else 0

def afficherProfilEleve(dico: dict, id: str):
    if id in dico:
        eleve = dico[id]
        print(f'ID: {id}, Nom: {eleve["nom"]}, Prénom: {eleve["prenom"]}, Âge: {eleve["age"]}')
        for matiere, notes in eleve['notes'].items():
            print(f'{matiere}: Moyenne = {calculerMoyenne(notes):.2f}')
    else:
        print('Élève introuvable.')

def menu():
    while True:
        choix = input("\n1: Ajouter élève\n2: Supprimer élève\n3: Afficher matières\n4: Ajouter matière\n5: Supprimer matière\n6: Afficher profil\n7: Quitter\nVotre choix: ")
        if choix == '1':
            creerEleve(gestionnaire)
        elif choix == '2':
            id = input("ID de l'élève: ")
            supprimerEleve(gestionnaire, id)
        elif choix == '3':
            id = input("ID de l'élève: ")
            afficherMatiere(gestionnaire, id)
        elif choix == '4':
            id = input("ID de l'élève: ")
            ajouterMatiere(gestionnaire, id)
        elif choix == '5':
            id = input("ID de l'élève: ")
            matiere = input('Nom de la matière: ')
            supprimerMatiere(gestionnaire, id, matiere)
        elif choix == '6':
            id = input("ID de l'élève: ")
            afficherProfilEleve(gestionnaire, id)
        elif choix == '7':
            break
        else:
            print('Choix invalide.')

if __name__ == "__main__":
    menu()