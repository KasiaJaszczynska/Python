import pygame as pg, sys, time
from pygame.locals import *

#ustawienia początkowe do gry(najwazniejsze zmienne)

czyjatura= 'x'
ktowygralgre= None
remis= False
szerokość= 500  #planszy
wysokość= 500

czarny = (255, 255, 255)
zielony = (0, 0, 0)
niebieski = (255, 0, 0)

punktyx= 0
punktyy= 0

plansza= [ [None] * 3, [None] * 3, [None] * 3 ]# plansza zawiera w sobie 3 mniejsze fragmenty (zawier 3 zmienne)
#okno programu
pg.init() #jest to funkcja, która inicjalizuje(pozostałe  funkcje)
FPS = 30

zegar = pg.time.clock()

ekran = pg.display.set_mode((szerokość, wysokość + 200), 0, 32)

pg.display.set_caption("kolko i krzyzyk")

planszastartowa = pg.image.load("plansza.png")
obrazekx= pg.image.load("krzyzyk.png")
obrazeko= pg.image.load("kółko.png")

# inne wymiaryobrazków

planszastartowa = pg.transfrom.scale (planszastartowa, (szerokosc, wysokosc + 200))
obraekx= pg.transfrom.scale (planszastartowa, (80, 80))
obrazeko= pg.transfrom.scale (planszastartowa, (80, 80))

def rysujplansze():  #mozna narysowac1 obrazek na 2 blit
                ekran.blit(planszastartowa, (0,0))
                
                pg.display.update()

rysujplansze()                
