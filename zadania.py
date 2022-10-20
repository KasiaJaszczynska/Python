import random

#print("Hello word") #to jest komentarz

#zmienna=10
#print(zmienna)

#print ("napis")
#print("napis1")
#print("napis2")

#print("Wartosci zmiennej to:")
#print (zmienna)

#print("Wartosc zminna to ", zmienna)
#print("wartosc zminnej to: %.2f" %zmienna)
#print(f"wartosc zmiennej to {zmienna}")
#print("Wartosc zmiennej to :"+ str(zmienna))


#wiek=int(input("ile masz lat")) #int ograniczemie dla tkownika moze podac tylko liczbe nie slownie


#suma=2+3
#roznica=4-2
#iloczyn=2*4
#iloraz=4/2

#reszta=5%2
#potega=2**4

ciag="napis"*10

print(ciag)

los=random.randint(1, 100)
print(los)
a=10
b=20

los1=random.randint(a, b)
print(los1)


if a>0:
    print("Zmienna jest wieksza od 0")

elif a==0:
    print("Zmienna jest równa 0")

else:
    print("Zmienna jest mniejsza od 0")


#los1=int(input("Podaj liczbę"))
#if a>0:
 #   print("Zmienna jest większa od 0 ")
#else:
 #   print("Zmienna jest miejsza od0 ")


#los1=int(input("Podaj licznę"))
#if a%2==0:
 #   print("Zmienna jest podzielna przez 2")

#else:    
 #   print("Zmienna nie jest podzielna przez 2 ")



#a=int(input("Podaj liczbę"))
#b=int(input("Podaj liczbę"))
#c=int(input("Podaj liczbę"))
#if a+b+c !=180:
 #   print("Taki trójkąt nie istnieje")
#elif  a== 0 or b==0 or c==0 :
 #   print("Taki trójkąt nie istnieje")

#else:
 #   if a<90 and b<90 and  c<90:
  #      print ("Trojkąt jest ostrokątny")
   # elif a== 90 or b==90 or c==90:    
    #    print ("Trojkąt jest prostokątny")
    #elif a>90 or b>90 or c<90:
     #   print ("Trojkąt jest rozwartokątny")

#i to inaczej licznik

print("---------")
for i in range(1, 10, 2):
    los=random.randint(1, 50)
    print(f"Wylosowana liczba nr {i+1} to {los}")

print("---------")
for i in range(100, 1 ,-1):
    los=random.randint(1, 50)
    print(f"Wylosowana liczba nr {i+1} to {los}")


for i in range(1, 101):
    if i%2==0:
        print("Liczby są podzielne przez 2")
    else:
        print("Liczby nie sa podzielne przez 2")

    
