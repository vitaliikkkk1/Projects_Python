from IPython.display import clear_output


def display_board(board):
    clear_output()

    print(board[7]+"|" + board[8] + '|' + board[9])
    print("-|-|-")
    print(board[4]+"|" + board[5] + '|' + board[6])
    print("-|-|-")
    print(board[1]+"|" + board[2] + '|' + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Which one do u want to play, X or O ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

print(player_input())


def place_marker(board, marker, position):

    board[position] = marker


print(place_marker(test_board, "$", 8))
print(display_board(test_board))



def win_check(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[7] == board [5] == board [3] == mark))


print (win_check(test_board,'X'))

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'





def space_check(board, position):

    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Select the next cell: (1-9) '))

    return position

def replay():

    return input('U want play again? Yes or No: ').lower().startswith('y')


import time
print('Welcome to the Tic Tac Toe game!')
time.sleep(0.2)

while True:
    # Настройка игры
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('He goes first ' + turn + '.')

    play_game = input('Are u ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Ход Игрока 1

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! U won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Ход Игрока 2

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
