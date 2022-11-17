import random
import string

def generuj_haslo (size= 7, chars=string.ascii_letters + string.digits +string.punctuation ):
    return ''.join(random.choice(chars) for _ in range(size))

haslo= int(input("Jak długie ma być hasło"))
print(generuj_haslo(haslo))