n = int(input("Entrez un nombre : "))
binaire = ""
while n > 0:
    binaire = str(n % 2) + binaire
    n = n // 2
print(binaire)