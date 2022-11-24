from random import randint as rnd

zakres= 19
los= 6



def losowanie ():
    losy = []
    for i in range (los):
        liczba = rnd(1, zakres)
        while liczba in losy: 
            liczba = rnd(1, zakres)
        losy.append(liczba)  #dodać
    return losy

def typowanie():
    typy=[]
    for i in range (los):
        while True:
            try:

                typ= int (input(f"Podaj liczbę od 1 do {zakres}"))
                if typ < 1 or typ > zakres:
                        print("Liczba jest poza zakresm! Podaj jeszcze raz: ")
                elif typ in typy:
                    print ("Ta liczba juz jest wytypowana. Podaj jeszcze raz")
                else:
                    break
            except:
                print("Podaj liczbę całkowatą")
        typy.append(typ)
    return typy


losy = losowanie()
losy.sort()
typy= typowanie()
typy.sort()


traf = 0
trafienia =()

for typ in typy:
    if typ in losy:
        traf +=1
        trafienia.append(typ)

print(f"Wylosowane liczby : {losy}")
print(f"Wytypowane liczby : {typy}")
print(f"Trafiłeś {traf} razy.")
print(f"Lista trafień: {trafienia}")

