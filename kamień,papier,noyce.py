import random
import time
import sys
name=(input("Podaj imię:"))

print("Jeśli chesz zakończy grę klikni 'k' ")
time.sleep(0.5)

while True:
    print()

    wybor=int(input("Wybierz: o- kamień,p papier , y- nozyce"))
    wybor_komp = random.randrange(o,p,y )
    o="kamień"
    p="papier"
    y="nozyce"

    print("3..")
    time.sleep(0.5)
    print("2..")
    time.sleep(0.5)
    print("1..")
    time.sleep(0.5)

    if wybor== o and wybor== o:
        print("o==o")
        time.sleep(0.5)
        print("Remis")
    elif wybor== o and wybor== y:
        print("o>y")
        time.sleep(0.5)
        print("Wygrywasz")
    elif wybor== o and wybor== p:
        print("o<p")
        time.sleep(0.5)
        print("Przegrywasz")
    elif wybor==k:
        print("Koniec gry")

    if wybor==p and wybor==p:
        print("p==p")
        time.sleep(0.5)
        print("Remis")
    elif wybor== p and wybor== o:
        print("p>o")
        time.sleep(0.5)
        print("Wygrywasz")
    elif wybor== p and wybor== y:
        print("p<y")
        time.sleep(0.5)
        print("Przegrywasz")
    elif wybor==k:
        print("Koniec gry")

    if wybor==y and wybor==y:
        print("y==y")
        time.sleep(0.5)
        print("Remis")
    elif wybor== y and wybor== p:
        print("y<p")
        time.sleep(0.5)
        print("Wygrywasz")
    elif wybor== y and wybor== o:
        print("y<o")
        time.sleep(0.5)
        print("Przegrywasz")
    elif wybor==k:
        print("Koniec gry")

    print()
    input("Wciśni  k jeśli chesz kontynuować")
         
