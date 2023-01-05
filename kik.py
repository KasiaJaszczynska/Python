def display_board(board):
    blankBoard="""
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
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

def player_input():
    player1 = input("Proszę wybrać 'X' lub 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("Wybrałeś/aś " + player1 + ". Gracz 2 będzie " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("Wybrałeś/aś " + player1 + ". Gracz 2 będzie " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Proszę wybrać 'X' lub 'O' ")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def player_choice(board):
    choice = input("Proszę wybrać wolne miejsce od 1 a 9 : ")
    while not space_check(board, int(choice)):
        choice = input("To miejsce nie jest wolne. Wybierz wolne miejsce od 1 do 9 : ")
    return choice

def replay():
    playAgain = input("Chcesz grać jeszcze raz tak/nie ? ")
    if playAgain.lower() == 'tak':
        return True
    if playAgain.lower() == 'nie':
        return False

if __name__ == "__main__":
    print('Witam, w grze kółko i krzyzyk!')
    i = 1
    # gracz wybiera swoją stronę
    players=player_input()
    # pusta tablica init
    board = ['#'] * 10
    while True:
        # tutaj usawiam grę
        game_on=full_board_check(board)
        while not game_on:
            # gracz tutaj wybiera miejsce znaku
            position = player_choice(board)
            # kot gra?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # graj
            place_marker(board, marker, int(position))
            # sprawdź tablicę
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("Wygrałeś/aś !")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # wybie swoja stronę
            players=player_input()
            # pusta tablica  init
            board = ['#'] * 10