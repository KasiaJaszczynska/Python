import random
name=input("Podaj imię:")



o="kamień"
p="papier"
y="nozyce"
k="koniec gry"   #gracz ybiera aby zakończyć grę


choose=("kamień", "papier", "nozyce")

while play:
    os.system("clear")
    print(intro)


    if wybor== o and wybor== o:
    print("o==o")
    print("Remis")
    elif wybor== o and wybor== y:
    print("o>y")
    print("Wygrywasz")
    elif wybor== o and wybor== p:
    print("o<p")
    print("Przegrywasz")
    elif wybor==k:
    print("Koniec gry")

    if wybor==p and wybor==p:
    print("p==p")
    print("Remis")
    elif wybor== p and wybor== o:
    print("p>o")
    print("Wygrywasz")
    elif wybor== p and wybor== y:
    print("p<y")
    print("Przegrywasz")
    elif wybor==k:
    print("Koniec gry")

    if wybor==y and wybor==y:
    print("y==y")
    print("Remis")
    elif wybor== y and wybor== p:
    print("y<p")
    print("Wygrywasz")
    elif wybor== y and wybor== o:
    print("y<o")
    print("Przegrywasz")
    elif wybor==k:
    print("Koniec gry")

