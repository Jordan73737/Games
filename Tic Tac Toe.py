from IPython.display import clear_output

#step 1
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(test_board)

#step 2
def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()
        print(1)
        print(marker)
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#step 3
def place_marker(board, marker, position):
    board[position] = marker

#place_marker(test_board,'$',8)
#display_board(test_board)

#step 4
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

win_check(test_board,'X')

#step 5

import random
def choose_first():
    #'0' is regarded as lesser or false compared to '1'
    #so if player roles random 1 then he gets to be player '1'
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#step 6
def space_check(board, position):
    return board[position] == ' '

#step 7
def full_board_check(board):
    for space in range(1,10):
        if space_check(board, space) == True:
            return False
    #if space available, that means board isn't full, therefore returning False
    #however, if you go through the loop and not return false, then you would return
    #true and break the loop because the board is full
    return True

#step 8
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board, position):
       position = int(input("Choose your next position: (1-9) "))
    return position

#step 9
def replay():
    return input("Would you like to play again? Say Yes or No?: ").lower().startswith('y')

#step 10
print('Welcome to Tic Tac Toe!')

still_playing = True
while still_playing == True:
    current_player = choose_first()
    print(current_player)
    marker = player_input()
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)
    turns = 0
    game_started = True
    while game_started:
        if current_player == "Player 1":
            if full_board_check(board) == False:
                position = player_choice(board)
                place_marker(board, marker[0], position)
                if win_check(board, marker[0]) == True:
                    print("Player 1 wins")
                    display_board(board)
                    break
                else:
                    display_board(board)
                    current_player = "Player 2"
            else:
                print("Draw")
                display_board(board)
                break
        else:
            if full_board_check(board) == False:
                position = player_choice(board)
                place_marker(board, marker[1], position)
                if win_check(board, marker[1]) == True:
                    print("Player 2 wins")
                    display_board(board)
                    break
                else:
                    display_board(board)
                    current_player = "Player 1"
            else:
                print("Draw")
                display_board(board)
                break

    if not replay():
        still_playing = False