#shows the board
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

#aks a player if they want to be an X or O
def player_input():
    player_marker = False
    
    while player_marker == False:
        marker= input('Please select if you want X/O:')
        
        if marker.uppercase() in ['X','O']:
            player_marker = True  
            return marker
                
        else:
            print("Please input a valide marker")

#Inputs the players marker on the board
def place_marker(board, marker, position):
    board[int(position)] = marker

#checks to see if the palyer won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))


#determines which player goes first
import random

def choose_first():
    return 'Player ' + str(random.randint(1,2)) 

#checks to make sure the space is avaiable 
def space_check(board, position):
    if board[position]== '':
        return True
    else:
        return False

#checks to make sure the game is not a draw
def full_board_check(board):
    for i in board:
        if i == '':
            return False
        else:
            continue 
    return True

#asks where the player wants to place their marker
def player_choice(board):
    loc = False
    
    while loc == False:
        desired_loc = input("Please pick a location to place your marker (1-9)")
        
        if desired_loc.isdigit()== True and int(desired_loc) in range(1,9) and space_check(board, int(desired_loc))== True:
            loc = True 
            return desired_loc
        else:
            print("Please input a location that is valid and not taken")

#after game is finishes asks to replay
def replay():
    play_again = input("Do you want to play again? Y/N")
    if play_again == 'Y':
        return True
    else:
        return False


#Instruction for games
# print('Welcome to Tic Tac Toe!')
game = True
#while True:
while game:
    # Set the game up here
    board = ['#','','','','','','','','','']
    
    print('Each player will now select their marker starting with Player 1 follow by Player 2')
    P1_marker = player_input()
    P2_marker = player_input()
        
    turn = choose_first()
    
    print(turn + ' will start')
    
    start = True

    while start: 
        # Player1's turn.
        if turn == 'Player 1':
            print('Player 1 turn:')
            position = player_choice(board)
            place_marker(board,P1_marker,position)
            display_board(board)
        
            if win_check(board, P1_marker):
                print('You won!')
                game = False
                start = False
            else: 
                if full_board_check(board):
                    print('That is all she wrote')
                    game = False
                else:
                    turn = 'Player 2'
        
        # Player2's turn.
        if turn == 'Player 2':
            print('Player 2 turn:')
            position = player_choice(board)
            place_marker(board,P2_marker,position)
            display_board(board)
        
            if win_check(board, P2_marker):
                print('You won!')
                game = False
                start = False
            else: 
                if full_board_check(board):
                    print('That is all she wrote')
                    game = False
                else:
                    turn = 'Player 1'

    #if not replay():
board = ['#','','','','','','','','','']
game = replay()