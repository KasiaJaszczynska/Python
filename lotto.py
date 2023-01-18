from random import randint as rnd

zakres : int = 19
los : int = 6

# kupienie losu w sklepie lotto
def typowanie():
    typy=[]
    for i in range (los):
        while True:
            try:

                typ= int (input(f"Podaj liczbę od 1 do {zakres} : \n "))
                if typ < 1 or typ > zakres:
                        print("Liczba jest poza zakresm! Podaj jeszcze raz: \n ")
                elif typ in typy:
                    print ("Ta liczba juz jest wytypowana. Podaj jeszcze raz: \n ")
                else:
                    break
            except:
                print("Podaj liczbę całkowatą")
        typy.append(typ)

    typy.sort()
    return typy

# komora losowani jest pusta, następuje zwolnienie blokady i rozpoczynamy losowanie <zakres> liczb
def losowanie ():
    losy = []
    for i in range (los):
        liczba = rnd(1, zakres)
        while liczba in losy: 
            liczba = rnd(1, zakres)
        losy.append(liczba)  #dodać

    losy.sort()
    return losy

# sprawdza wyniki losowania
def sprawdzTrafienia(typy, losy):
    traf = 0
    trafienia = []

    for typ in typy:
        if typ in losy:
            traf +=1
            trafienia.append(typ)

    print(f"Wylosowane liczby : {losy}")
    print(f"Wytypowane liczby : {typy}")
    print(f"Trafiłeś {traf} razy.")
    print(f"Lista trafień: {trafienia}")



typy = typowanie()

losy = losowanie()

sprawdzTrafienia(typy, losy)