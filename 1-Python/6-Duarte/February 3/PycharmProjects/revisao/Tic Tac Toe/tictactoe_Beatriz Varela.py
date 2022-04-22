# Tic-Tac-Toe (2-Players)

'''
The board is a dictionary in which keys will be the location.
Initially, the values will be empty spaces. After every move,
the value will change according to the player's choice.
'''

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

'''
The board will be printed after every move through the function printBoard.
'''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


'''
The function game has all the gameplay functionality.
'''

player1 = input("Player 1, what's your name?")
print(player1, ", you will play as X")
player2 = input("Player 2, what's your name?")
print(player2, ", you will play as 0")


def game():
    turn = "X"
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn,", turn, ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        '''
        Checking if player X or O has won, for every move after 5 moves.
        '''
        if count >= 5:
            # across the top
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # across the middle
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # across the bottom
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # down the left side
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # down the middle
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # down the right side
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # diagonal 1
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            # diagonal 2
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        '''
        If neither X nor O wins and the board is full, a tie is declared.
        '''
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        '''
        Also, player 1 takes turns with player 2.  
        '''
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    '''
    At the end of the game, the program will ask the player if they want to restart the game.
    '''
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


'''
Let's play a game...
'''
if __name__ == "__main__":
    game()
