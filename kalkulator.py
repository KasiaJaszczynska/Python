import math
def dodaj(a, b):
    return a+b

dzialanie=input("Jakie działanie chcesz wykonać?  + dodawanie, - odjemowanie, * mnoenie, / dzielnik, ^ potęgowanie, a ** (1/stopien) pierwiastek")

a=int(input("Podaj pierwszą liczbę:"))
b=int(input("Podaj drugą liczbę:"))

if dzialanie=="+":
    wynik=a+b
    print("Wynik dodawania to:", wynik)
elif dzialanie=="-":
    wynik=a-b
    print("Wynik odejmowania to:", wynik)
elif dzialanie=="*":
    wynik=a*b
    print("Wynik mnozenia to:", wynik)
elif dzialanie=="/":
    while b==0:
        print("Nie dziel przez 0")
        b=int(input("Podaj liczbę jecze raz :"))
    wynik=a/b
    print("Wynik dzielenia to:", wynik)

    #if b==0:
     #   print("Nie mona dzielić przez 0")
    #else:
     #   wynik=a/b
      #  print("Wynik dzielenia to:", wynik)

#elif dzialanie =="** (1/stopien)":
 #   wynik= a ** (1/b)
  #  print("Wynik działania to:", wynik)

elif dzialanie=="^":
    wynik=a**b
    print("Wynik potęgowania to:", wynik)
else:
    print("Niewłaściwy znak") 

def pierwiastek(a, stopien):
    wynik = a ** (1 / stopien)
    return wynik
