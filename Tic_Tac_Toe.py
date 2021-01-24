'''
Tic Tac Game
'''
import random

#Welcome Message ###

print('Welcome To Tic Tac Toe Game')

def player_input():
    '''
    Selecting Players Marker
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        #Asking for their markers
        marker = input("Please choose your mark 'O' or 'X' ")
    player1_marker = marker
    # Deciding Marks for each player
    if player1_marker == 'O':
        final = ['O', 'X']
    else:
        final = ['X', 'O']
    return final
def choose_first():
    '''
    Randomply selects players choice
    '''
    if random.randint(0, 1) == 0:
        result = 'Player_1'#returns player 1
    else:
        result = 'Player_2'#returns player 2
    return result
def board_display(board):
    '''
    Display Users Board
    '''
    print('\n'*100)
    print('---------------------')
    print('                     ')
    print('  '+board[7]+'  '+' | '+'  '+board[8]+'  '+' | '+'  '+board[9])
    print('                     ')
    print('=====================')
    print('           ')
    print('  '+board[4]+'  '+' | '+'  '+board[5]+'  '+' | '+'  '+board[6])
    print('           ')
    print('=====================')
    print('                     ')
    print('  '+board[1]+'  '+' | '+'  '+board[2]+'  '+' | '+'  '+board[3])
    print('                     ')
    print('---------------------')
def player_choice(theboard):
    '''
    Player selecting their position
    '''
    position = 0
    while (position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]) or (not space_check(theboard, position)):
        position = int(input('Please pick a position from (1-9)'))
        return position
def space_check(board, position):
    '''
    space checker
    '''
    return board[position] == ' '
def full_board_check(board):
    '''
    board space checker
    '''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
def win_check(board, mark):
    '''
    checking if anyone won or not
    '''
    return  (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark)
def place_marker(board, marker, position):
    '''
    Marker Position
    '''
    board[position] = marker
def replay():
    '''
    loop stopper
    '''
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    #while Loop to make this game continuously played 
while True:
    theboard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    ready = input('Are You ready to play Y for yes and N for no ').upper()
    if ready == 'Y':
        game_start = True
    elif ready == 'N':
        game_start = False
    while game_start == True:
        # Player 1 turn
        if turn == 'Player_1':
            board_display(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
            #win check
            if win_check(theboard, player1_marker):
                board_display(theboard)
                print('Congrats! Player 1 has Won')
                break
                game_start = False
            else:
                if full_board_check(theboard):
                    board_display(theboard)
                    print('It a Tie no one won the game')
                    break
                else:
                    turn = 'Player_2'
        elif turn == 'Player_2':
            #player2 Turn
            board_display(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)
            #win check
            if win_check(theboard, player2_marker):
                board_display(theboard)
                print('Congrats! Player 1 has Won')
                break
                game_start = False
            else:
                if full_board_check(theboard):
                    board_display(theboard)
                    print('It a Tie no one won the game')
                    break
                else:
                    turn = 'Player_1'
    # used to break out of loop
    if not replay():
        break
# Thanking Player ##
print('Thanks For Playing This Game')

end = input('Press return key to exit')
