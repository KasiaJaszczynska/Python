import pygame as pg, sys, time
from pygame.locals import *

#ustawienia początkowe do gry(najwazniejsze zmienne)

czyjatura= 'x'
ktowygralgre= None
remis= False
szerokość= 500  #planszy
wysokość= 500

czarny = (255, 255, 255)
zielony = (0, 0, ,0)
niebieski = (255, 0, 0)

punktyx= 0
punktyy= 0

plansza= [ [None] * 3, [None] * 3, [None] * 3 ]# plansza zawiera w sobie 3 mniejsze fragmenty (zawier 3 zmienne)
#okno programu
pg.init() 

