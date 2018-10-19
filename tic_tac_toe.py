import random as r
import sys

board = [0,1,2,
         3,4,5,
         6,7,8]

def show():
    print(' ',     '|',   ' ',  '|'         )
    print(board[0],'|',board[1],'|',board[2])
    print(' ',     '|',   ' ',  '|'         )
    print('-----------'                     )
    print(' ',     '|',   ' ',  '|'         )
    print(board[3],'|',board[4],'|',board[5])
    print(' ',     '|',   ' ',  '|'         )
    print('-----------'                     )
    print(' ',     '|',   ' ',  '|'         )
    print(board[6],'|',board[7],'|',board[8])
    print(' ',     '|',   ' ',  '|',    "\n")

# Printing instructions
def instructions():
    print("Instructions: ")
    print("1. You can choose from player 2 is playing or opponent is playing"             )
    print("2. Player(Default) is always 'X' and player 2 or opponent is 'O'"              )
    print("3. On the board there will be numbers, program will ask you for a number input")
    print("4. This is still WIP\n"                                                        )
    
running = True

# Needed in input logic
print_count = True

# While ask; asks player if player 2 is playing
ask = True

while running:

    if ask == True:
        instructions()
        player_2_play = input("Is player 2 playing? Y/N: ").upper()

    if player_2_play == 'Y':
        player_2_turn = True
        player_turn = True

        print_count = (print_count)
        
        ask = False

        while player_turn == True:

            if print_count == True:
                print("Player 2 is playing...\n")
                print_count = False

            player_input = int(input("Player you are 'X', Input a number(0-8): "))

            # If player_input is not in arr[] loops input
            while player_input > 8 or player_input < 0:
                print("Invalid Move\n")
                player_input = int(input("Player you are 'X', Input a number: "))

            if board[player_input] != 'X' and board[player_input] != 'O':      
                board[player_input] = 'X'

                print("Player's Turn\n")

                player_turn = False
                player_2_turn = True
                    
                # Across win
                if board[0] == board [1] and board[1] == board[2]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                elif board[3] == board[4] and board[4] == board[5]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                elif board[6] == board[7] and board[7] == board[8]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                # Vertical win
                elif board[0] == board[3] and board[3] == board[6]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                elif board[1] == board[4] and board[4] == board[7]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                elif board[2] == board[5] and board[5] == board[8]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                # Diagonal win
                elif board[0] == board[4] and board[4] == board[8]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                elif board[2] == board[4] and board[4] == board[6]:
                    print("PLAYER WINS!!!")
                    show()
                    sys.exit()

                # If board[inputs] does not = to board[original outputs]:
                elif (board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
                    print('Tie')
                    sys.exit()

                else:
                    pass

            elif board[player_input] == 'X' or board[player_input] == 'O':
                print('Spot is taken\n')

                player_2_turn = False
                player_turn = True

            show()

        while player_2_turn == True:
            player_input_2 = int(input("Player 2 you are 'O', Input a number(0-8): "))

            # If player_input_2 is not in arr[] loops input
            while player_input_2 > 8 or player_input_2 < 0:
                print("Invalid Move\n")
                player_input_2 = int(input("Player you are 'X', Input a number(0-8): "))

            if board[player_input_2] != 'X' and board[player_input_2] != 'O':      
                board[player_input_2] = 'O'

                print("Player 2's Turn\n")

                player_turn = True
                player_2_turn = False
                
                # Across win
                if board[0] == board [1] and board[1] == board[2]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                elif board[3] == board[4] and board[4] == board[5]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                elif board[6] == board[7] and board[7] == board[8]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                # Vertical win
                elif board[0] == board[3] and board[3] == board[6]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                elif board[1] == board[4] and board[4] == board[7]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                elif board[2] == board[5] and board[5] == board[8]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                # Diagonal win
                elif board[0] == board[4] and board[4] == board[8]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                elif board[2] == board[4] and board[4] == board[6]:
                    print("PLAYER 2 WINS!!!")
                    show()
                    sys.exit()

                # If board[inputs] does not = to board[original outputs]:
                elif (board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
                    print('Tie')
                    sys.exit()
                    
                else:
                    pass

            elif board[player_input] == 'X' or board[player_input] == 'O':
                print('Spot is taken\n')

                player_2_turn = True
                player_turn = False

    elif player_2_play == 'N':
        player_turn = True
        opponent_turn = True

        ask = False

        while player_turn == True:     
            player_input = int(input("Player you are 'X', Input a number(0-8): "))

            # If player_input is not in arr[] loops input
            while player_input > 8 or player_input < 0:
                print("Invalid Move\n")
                player_input = int(input("Player you are 'X', Input a number(0-8): "))

            if board[player_input] != 'X' and board[player_input] != 'O':      
                board[player_input] = 'X'

                print("Player's Turn\n")

                player_turn = False
                opponent_turn = True
                
                # Across win
                if board[0] == board [1] and board[1] == board[2]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                elif board[3] == board[4] and board[4] == board[5]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                elif board[6] == board[7] and board[7] == board[8]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                # Vertical win
                elif board[0] == board[3] and board[3] == board[6]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                elif board[1] == board[4] and board[4] == board[7]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                elif board[2] == board[5] and board[5] == board[8]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                # Diagonal win
                elif board[0] == board[4] and board[4] == board[8]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                elif board[2] == board[4] and board[4] == board[6]:
                    print("YOU WIN!!!")
                    show()
                    sys.exit()

                # If board[inputs] does not = to board[original outputs]:
                elif (board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
                    print('Tie')
                    sys.exit()
                    
                else:
                    pass

            elif board[player_input] == 'X' or board[player_input] == 'O':
                print('Spot is taken\n')

                opponent_turn = False
                player_turn = True

            show()

        while opponent_turn == True:
            r.seed()
            opponent_input = r.randint(0,8)

            if board[opponent_input] != 'O' and board[opponent_input] != 'X':
                board[opponent_input] = 'O'

                print('Opponents turn\n')
                print("Opponent chose:", opponent_input,"\n")

                opponent_turn = False
                player_turn = True

                # Across win
                if board[0] == board [1] and board[1] == board[2]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                elif board[3] == board[4] and board[4] == board[5]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                elif board[6] == board[7] and board[7] == board[8]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                # Vertical win
                elif board[0] == board[3] and board[3] == board[6]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                elif board[1] == board[4] and board[4] == board[7]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                elif board[2] == board[5] and board[5] == board[8]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                # Diagonal win
                elif board[0] == board[4] and board[4] == board[8]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                elif board[2] == board[4] and board[4] == board[6]:
                    print("YOU LOSE!!! :(")
                    show()
                    sys.exit()

                # If board[inputs] does not = to board[original outputs]:
                elif (board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
                    print('Tie')
                    sys.exit()
                                
                else:
                    pass

            elif board[opponent_input] == 'O' or board[opponent_input] == 'X':

                opponent_turn = True
                player_turn = False

    elif player_2_play != 'Y' or player_2_play != 'N':
        player_2_play

##    if (board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
##        print('Tie')
##        #sys.exit()

    if ask == False:
        show()

