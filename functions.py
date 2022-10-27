from random import random


import random

def powitanie(imie):
    print("Cześć,", imie )

def wartoscbezwgledna(liczba):
    if liczba>=0:
        return liczba
    else:
        return -liczba

imie=input("Jak masz na imię?")
powitanie(imie)
print(wartoscbezwgledna(-10))


