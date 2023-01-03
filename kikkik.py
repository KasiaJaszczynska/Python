def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for  i  in range ( 1 , 10 ):
        if ( tablica [ i ] ==  'O'  lub  tablica [ i ] ==  'X' ):
            pusta tablica  =  pusta tablica . zastąpić ( str ( i ), tablica [ i ])
        inaczej :
            pusta tablica  =  pusta tablica . zastąp ( str ( i ), ' ' )
    drukuj ( pusta tablica )

def  player_input ():
    player1  =  input ( "Proszę wybrać znacznik 'X' lub 'O' " )
    podczas gdy  Prawda :
        jeśli  gracz1 . górny () ==  'X' :
            gracz2 = 'O'
            print ( "Wybrałeś "  + player1 + " . Gracz 2 będzie " +  player2  )   
            zwróć  gracza 1 . górny (), gracz2
        elif  player1 . górny () ==  'O' :
            gracz2 = 'X'
            print ( "Wybrałeś "  + player1 + " . Gracz 2 będzie " +  player2  )   
            zwróć  gracza 1 . górny (), gracz2
        inaczej :
            player1  =  input ( "Proszę wybrać znacznik 'X' lub 'O' " )

def  place_marker ( plansza , znacznik , pozycja ):
    tablica [ pozycja ] =  znacznik
     tablica zwrotna

def  space_check ( plansza , pozycja ):
    zwróć  planszę [ pozycja ] ==  '#'

def  full_board_check ( tablica ):
    return  len ([ x  for  x  in  board  if  x  ==  '#' ]) ==  1

def  win_check ( tablica , znak ):
    if  plansza [ 1 ] ==  plansza [ 2 ] ==  plansza [ 3 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 4 ] ==  plansza [ 5 ] ==  plansza [ 6 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 7 ] ==  plansza [ 8 ] ==  plansza [ 9 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 1 ] ==  plansza [ 4 ] ==  plansza [ 7 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 2 ] ==  plansza [ 5 ] ==  plansza [ 8 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 3 ] ==  plansza [ 6 ] ==  plansza [ 9 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 1 ] ==  plansza [ 5 ] ==  plansza [ 9 ] ==  zaznacz :
        zwróć  Prawda
    if  plansza [ 3 ] ==  plansza [ 5 ] ==  plansza [ 7 ] ==  zaznacz :
        zwróć  Prawda
    powrót  Fałsz

def  wybór_gracza ( plansza ):
    choice  =  input ( "Proszę wybrać puste miejsce między 1 a 9: " )
    podczas gdy  nie  space_check ( board , int ( choice )):
        choice  =  input ( "To miejsce nie jest wolne. Wybierz od 1 do 9: " )
    zwrotny  wybór

def  replay ():
    playAgain  =  input ( "Czy chcesz zagrać ponownie (t/n)? " )
    jeśli  zagraj ponownie . niższy () ==  'y' :
        zwróć  Prawda
    jeśli  zagraj ponownie . niższy () ==  'n' :
        powrót  Fałsz

if  __name__  ==  "__main__" :
    print ( 'Witamy w kółko i krzyżyk!' )
    ja  =  1
    # Wybierz swoją stronę
    gracze = wejście_gracza ()
    # Pusta tablica init
    plansza  = [ '#' ] *  10
    podczas gdy  Prawda :
        # Ustaw grę tutaj
        game_on = full_board_check ( plansza )
        podczas gdy  nie  game_on :
            # Gracz, aby wybrać, gdzie umieścić znak
            pozycja  =  wybór_gracza ( plansza )
            # Kto gra?
            jeśli  ja  %  2  ==  0 :
                znacznik  =  gracze [ 1 ]
            inaczej :
                znacznik  =  gracze [ 0 ]
            # graj
            place_marker ( plansza , znacznik , int ( pozycja ))
            # Sprawdź tablicę
            display_board ( tablica )
            ja  +=  1
            if  win_check ( tablica , znacznik ):
                print ( "Wygrałeś!" )
                złamać
            game_on = full_board_check ( plansza )
        if not replay():
            break
        else :
            i  =  1
            # Wybierz swoją stronę
            gracze = gracz_input ()
            # Pusta tablica init
            plansza  = [ '#' ] *  10