import random

a = random.randint(0, 100)
b = int(input("Entrez un nombre entre 0 et 100 : "))
while b != a:
  if b > a:
    print("Trop haut")
  if b < a:
    print("Trop petit")
  b = int(input("Entrez un nombre entre 0 et 100 : "))
print("You guessed it!")
