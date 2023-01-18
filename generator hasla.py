import random
import string

def generuj_haslo (rozmiar= 7, znaki=string.ascii_letters + string.digits +string.punctuation ):
    return ''.join(random.choice(znaki) for _ in range(rozmiar))

haslo= int(input("Jak długie ma być hasło: \n"))
print(generuj_haslo(haslo))