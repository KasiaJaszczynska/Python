from random import randint
tools=["kamień", "papier", "nozyczki"] #narzeędzia

wyniki= {("papier", "nozyczki"): "nozyczki",
         ("papier", "kamień" ) : "papier",
         ("kamień", "nozyczki"): "kamień"}

wybor_gracza=input("kamień, papier czy nozyczki")
if wybor_gracza not in tools:
    raise Exception ("Unknown tools") # podnieść wymagania dotyczące wyboru gracza

wybor_komp=tools[randint (0,2)]
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
