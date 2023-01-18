import math

dzialanie = input("Jakie działanie chcesz wykonać? " +
"+ dodawanie, - odjemowanie, * mnozenie, / dzielnik, ^ potęgowanie, -- pierwiastek, % reszta z dzielenia, // dzielenie bez reszty:  ")

a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))

if dzialanie == "+":
    wynik = a+b

elif dzialanie=="-":
    wynik = a-b

elif dzialanie=="*":
    wynik=a*b

elif dzialanie=="/":
    while b==0:
        print("Nie dziel przez 0")
        b=int(input("Podaj liczbę jecze raz :"))
    wynik=a/b

elif dzialanie== "--":
    wynik = pow(a, 1/b)

elif dzialanie=="^":
    wynik=pow(a, b)  

elif dzialanie== "%":
    wynik = a % b

elif dzialanie=="//":  
    wynik=a // b  

else:
    print("Niewłaściwy znak") 


print("Wynik działania to: ", wynik)