n = int(input("Entrez le nombre d'étages souhaité : "))
for i in range(1, n + 1):
    espaces = ' ' * (n - i)
    etoiles = '*' * (2 * i - 1)
    print(espaces + etoiles)