notes = []
while True:
    entree = input("Entrez des note et appuyer sur 'Q' pour quitter : ")
    if entree.upper() == 'Q':
        break
    try:
        note = float(entree)
        if 0 <= note <= 20:
            notes.append(note)
        else:
            print("Note invalide !")
    except ValueError:
        print("Entrée invalide !")
print("Notes valides :", notes)