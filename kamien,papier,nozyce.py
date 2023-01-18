from random import randint

narzędzia=["kamien", "papier", "nozyczki"] #narzeędzia

wyniki= {("papier", "nozyczki"): "nozyczki",
         ("papier", "kamien" ) : "papier",
         ("kamien", "nozyczki"): "kamien"}

wybor_gracza=input("kamien, papier czy nozyczki: \n")
if wybor_gracza not in narzędzia:
    raise Exception ("Nieznane narzędzia") # podnieść wymagania dotyczące wyboru gracza

wybor_komp=narzędzia[randint (0,2)]
print(wybor_komp)

if wybor_gracza==wybor_komp:
    print ("Remis")
else:
    for wynik in wyniki:
        if wybor_gracza in wynik and wybor_komp in wynik:
            zwycięsca = wyniki[wynik]
            if wybor_gracza== zwycięsca:
                print("Wygrałeś")
            else:
                print("Przegrałeś")
            break
