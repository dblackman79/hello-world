"""
Project #1: A Simple Game

*************************
*                       *
*      Connect 4        *
*    70 Ways To Win     *
*                       *
*************************
"""

def display_board(board):
    print(board[1][5]+'|'+board[2][5]+'|'+board[3][5]+'|'+board[4][5]+'|'+board[5][5]+'|'+board[6][5]+'|'+board[7][5])
    print(board[1][4]+'|'+board[2][4]+'|'+board[3][4]+'|'+board[4][4]+'|'+board[5][4]+'|'+board[6][4]+'|'+board[7][4])
    print(board[1][3]+'|'+board[2][3]+'|'+board[3][3]+'|'+board[4][3]+'|'+board[5][3]+'|'+board[6][3]+'|'+board[7][3])
    print(board[1][2]+'|'+board[2][2]+'|'+board[3][2]+'|'+board[4][2]+'|'+board[5][2]+'|'+board[6][2]+'|'+board[7][2])
    print(board[1][1]+'|'+board[2][1]+'|'+board[3][1]+'|'+board[4][1]+'|'+board[5][1]+'|'+board[6][1]+'|'+board[7][1])
    print(board[1][0]+'|'+board[2][0]+'|'+board[3][0]+'|'+board[4][0]+'|'+board[5][0]+'|'+board[6][0]+'|'+board[7][0])
    print("-------------")
    print("1|2|3|4|5|6|7")


game_board = [['$','$','$','$','$','$'],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
player1 = 'X'#u'\u2B23'
player2 = 'O'#u'\u2B22'

def game_check(board):
    for x in range(1,5):
        for y in range(6):
        #all rows (25 solutions)
            if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] == currentPlayer:
                return True
    for x in range(3):
        for y in range(1,8):
        #all columns (21 solutions)
            if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3] == currentPlayer:
                return True
    for x in range(1,5):
        for y in range(3):
            #diagnols (top-right (12 solutions))
            if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == currentPlayer:
                return True
    for x in range(4,8):
        for y in range(3):
            #diagnols (top-left (12 solutions))
            if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] == currentPlayer:
                return True

def player_turn():
    display_board(game_board)
    choice = int(input(f"{currentPlayer}, please pick your column number: 1-7"))
    while choice not in range(1,8):
        choice = int(input(f"{currentPlayer}, please pick your column number: 1-7"))
    for x,space in enumerate (game_board[choice]):
        if space == ' ':
            game_board[choice][x] = currentPlayer
            break
    display_board(game_board)

while True:
    currentPlayer = player1
    whoPlayer = 1
    game_On = True
    while game_On:
        player_turn()
        if game_check(game_board) == True:
            print(f"{currentPlayer} wins!")
            game_On = False
            break
        else:
            whoPlayer += 1
            if whoPlayer % 2 == 0:
	            currentPlayer=player2
            else:
	            currentPlayer=player1
    result = input("Do you want to play again? Y or N").lower()
    if result == 'y':
        game_On = True
        game_board = [['$','$','$','$','$','$'],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
        continue
    else:
        break