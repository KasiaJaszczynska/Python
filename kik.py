def wyswietlacz(tablica):
    pustatablica="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|_________________|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|_________________|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|_________________|
"""

    for i in range(1,10):
        if (tablica[i] == 'O' or tablica[i] == 'X'):
            pustatablica = pustatablica.replace(str(i), tablica[i])
        else:
            pustatablica = pustatablica.replace(str(i), ' ')
    print(pustatablica)

# Prosi uzytkownika o wybranie X lub O na cala gre
def wejscie_gracza():
    gracz1 = input("Proszę wybrać 'X' lub 'O'  \n")
    while True:
        if gracz1.upper() == 'X':
            gracz2= 'O'
            print("Wybrałeś/aś " + gracz1 + ". Gracz 2 będzie " + gracz2)
            return gracz1.upper(), gracz2 
        elif gracz1.upper() == 'O':
            gracz2='X'
            print("Wybrałeś/aś " + gracz1 + ". Gracz 2 będzie " + gracz2)
            return gracz1.upper(), gracz2 
        else:
            gracz1 = input("Proszę wybrać 'X' lub 'O'  \n ")


def znacznik_miejsca(tablica, znacznik, pozycja):
    tablica[pozycja] = znacznik
    return tablica

def sprawdzenie_przestrzeni(tablica, pozycja):
    return tablica[pozycja] == '#'

def pelne_sprawdzenie_tablicy(tablica):
    return len([x for x in tablica if x == '#']) == 1

def sprawdzenie_wygranej(tablica, znak):
    if tablica[1] == tablica[2] == tablica[3] == znak:
        return True
    if tablica[4] == tablica[5] == tablica[6] == znak:
        return True
    if tablica[7] == tablica[8] == tablica[9] == znak:
        return True
    if tablica[1] == tablica[4] == tablica[7] == znak:
        return True
    if tablica[2] == tablica[5] == tablica[8] == znak:
        return True
    if tablica[3] == tablica[6] == tablica[9] == znak:
        return True
    if tablica[1] == tablica[5] == tablica[9] == znak:
        return True
    if tablica[3] == tablica[5] == tablica[7] == znak:
        return True
    return False

def wybor_gracza(tablica):
    wybor = input("Proszę wybrać wolne miejsce od 1 a 9 : \n ")
    while not sprawdzenie_przestrzeni(tablica, int(wybor)):
        wybor = input("To miejsce nie jest wolne. Wybierz wolne miejsce od 1 do 9 : \n ")
    return wybor

def powtorna_rozgrywka():
    zagraj_ponownie = input("Chcesz grać jeszcze raz tak/nie ? \n ")
    if zagraj_ponownie.lower() == 'tak':
        return True
    if zagraj_ponownie.lower() == 'nie':
        return False

if __name__ == "__main__":
    print('Witam, w grze kółko i krzyzyk!')
    i = 1
    # gracz wybiera swoją stronę
    gracze=wejscie_gracza()
    # pusta tablica init
    tablica = ['#'] * 10
    while True:
        # tutaj usawiam grę
        właczona_gra=pelne_sprawdzenie_tablicy(tablica)
        while not właczona_gra:
            # gracz tutaj wybiera miejsce znaku
            pozycja = wybor_gracza(tablica)
            # kto gra?
            if i % 2 == 0:
                znacznik = gracze[1]
            else:
                znacznik = gracze[0]
            # graj
            znacznik_miejsca(tablica, znacznik, int(pozycja))
            # sprawdź tablicę
            wyswietlacz(tablica)
            i += 1
            if sprawdzenie_wygranej(tablica, znacznik):
                print("Wygrałeś/aś !")
                break
            właczona_gra=pelne_sprawdzenie_tablicy(tablica)
        if not powtorna_rozgrywka():
            break
        else:
            i = 1
            # wybie swoja stronę
            gracze=wejscie_gracza()
            # pusta tablica  init
            tablica = ['#'] * 10