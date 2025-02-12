gestionnaire = {
    'TFerragu': {
        'nom': 'Ferragu',
        'prenom': 'Thomas',
        'age': 25,
        'notes': {
            'Maths': [
                12,
                14
            ],
            'NSI': [
                14,
                17,
                15
            ],
            'Physique': [
                20,
                20
            ]
        }
    },
    'BLéa': {
        'nom': 'Léa',
        'prenom': 'BARBERON',
        'age': 25,
        'notes': {
            'Maths': [
                20,
                14
            ],
            'NSI': [
                20,
                14,
                20,
                20
            ],
            'Physique': []
        }
    }
}

def getIdentifiant(nom : str, prenom : str) -> str :
    """
    Retourne l'identfiant de l'élève depuis son nom prenom

    Args:
        nom (str): le nom de l'élève
        prenom (str): le prénom de l'élève

    Returns:
        str: son identidiant
    """
    return prenom[0] + nom[0:8]

def ajouterEleves(dico: dict) -> str:
    """
    Demande à l'utilisateur nom, prenom, age, et
    ajoute ce nouvel élève dans le dico de gestion.

    Un élève est représenté par un dico :

    'TFerragu': {
        'nom': 'Ferragu',
        'prenom': 'Thomas',
        'age': 25,
        'notes': {}
    }

    Args:
        dico (dict): dico de gestion

    Returns:
        str: l'id de l'élève
    """
    assert isinstance(dico, dict)
    assert isinstance(id, str | None)

    nom    = input('nom    : ')
    prenom = input('prenom : ')
    age    = int(input('age    : '))
    id     = getIdentifiant(nom, prenom)
    dico[id] = {
        'nom': nom,
        'prenom': prenom,
        'age': age,
        'notes': {}
    }
    return id

def supprimerEleve(dico: dict, id: str = None) -> None:
    """
    Demande l'identifiant d'un élève et supprime
    cet élève du dictionnaire de gestion.

    l'id peut optionnellement être passé en paramètre.

    Args:
        dico (dict): le dico de gestion
        id (str, optional): id. None par défaut.
    """
    assert isinstance(dico, dict)
    assert isinstance(id, str | None)

def descriptionEleve(dico: dict, id: str = None) -> str:
    """
    Demande l'identifiant d'un élève et retourne
    toutes les informations de cet élève.

    l'id peut optionnellement être passé en paramètre.

    Args:
        dico (dict): le dico de gestion
        id (str, optional): id. None par défaut.

    Returns:
        str: la description de l'élève
    """
    assert isinstance(dico, dict)
    assert isinstance(id, str | None)

def ajouterMatiere(dico: dict, id: str = None) -> None:
    """
    Demande l'identifiant d'un élève, puis demande
    le nom d'une matière, et enfin demande de saisir
    toutes les notes de l'élève dans cette matière.

    Ajoute toutes ces informations dans le dico de gestion.

    l'id peut optionnellement être passé en paramètre.

    Args:
        dico (dict): le dico de gestion
        id (str, optional): id. None par défaut.
    """
    assert isinstance(dico, dict)
    assert isinstance(id, str | None)

def supprimerMatiere(dico: dict, id: str = None) -> None:
    """
    Demande l'identifiant d'un élève, puis demande
    le nom d'une matière, et supprime les infos liées
    à cette matière.

    l'id peut optionnellement être passé en paramètre.

    Args:
        dico (dict): le dico de gestion.
        id (str, optional): id. None par défaut.
    """
    assert isinstance(dico, dict)
    assert isinstance(id, str | None)

    if not id :
        id = input('id : ')
    return id if id in dico else None