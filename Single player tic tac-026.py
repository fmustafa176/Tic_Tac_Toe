import time     # makes the game look better
import random   # for toss
def print_board(board):   # prints the grid for the game
    print(f" {board[0]} | {board[1]} | {board[2]} \n---+---+---\n {board[3]} | {board[4]} | {board[5]} \n---+---+---\n {board[6]} | {board[7]} | {board[8]} ")
# uploaded 
def is_winner(board, symbol):   # checks if any winning conditions are met after every turn. Returns True if they are
    # check the rows
    if board[0] == board[1] == board[2] == symbol:
        return True
    if board[3] == board[4] == board[5] == symbol:
        return True
    if board[6] == board[7] == board[8] == symbol:
        return True
    # check the columns
    if board[0] == board[3] == board[6] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True
    # check the diagonals
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    # otherwise, no winner
    return False

def is_draw(board):    # checks for draw condition
    for x in board:
        if isinstance(x, int):    # this is checking if any of the boxes on the grid is still not a X or O
            return False
    return True

def computer_move(board, comp_sign):    # the brain of the computer
    sides = [1, 3, 5, 7]
    # for row 1
    if board[0] == board[1] and isinstance (board[2],int):
        board[2] = comp_sign
        return board
    elif board[0] == board[2] and isinstance (board[1],int):
        board[1] = comp_sign
        return board
    elif board[1] == board[2] and isinstance (board[0],int):
        board[0] = comp_sign
        return board
    # for row 2
    elif board[3] == board[4] and isinstance (board[5],int):
        board[5] = comp_sign
        return board
    elif board[3] == board[5] and isinstance (board[4],int):
        board[4] = comp_sign
        return board
    elif board[4] == board[5] and isinstance (board[3],int):
        board[3] = comp_sign
        return board
    # for row 3
    elif board[6] == board[7] and isinstance (board[8],int):
        board[8] = comp_sign
        return board
    elif board[6] == board[8] and isinstance (board[7],int):
        board[7] = comp_sign
        return board
    elif board[7] == board[8] and isinstance (board[6],int):
        board[6] = comp_sign
        return board
    # for column 1
    elif board[0] == board[3] and isinstance (board[0],int):
        board[6] = comp_sign
        return board
    elif board[3] == board[6] and isinstance (board[0],int):
        board[0] = comp_sign
        return board
    elif board[6] == board[0] and isinstance (board[3],int):
        board[3] = comp_sign
        return board
    # for column 2
    elif board[1] == board[4] and isinstance (board[7],int):
        board[7] = comp_sign
        return board
    elif board[4] == board[7] and isinstance (board[1],int):
        board[1] = comp_sign
        return board
    elif board[7] == board[1] and isinstance (board[4],int):
        board[4] = comp_sign
        return board
    # for column 3
    elif board[2] == board[5] and isinstance (board[8],int):
        board[8] = comp_sign
        return board
    elif board[5] == board[8] and isinstance (board[2],int):
        board[2] = comp_sign
        return board
    elif board[2] == board[8] and isinstance (board[5],int):
        board[5] = comp_sign
        return board
    # for diagonal 1 
    elif board[0] == board[4] and isinstance (board[8],int):
        board[8] = comp_sign
        return board
    elif board[4] == board[8] and isinstance (board[0],int):
        board[0] = comp_sign
        return board
    elif board[8] == board[0] and isinstance (board[4],int):
        board[4] = comp_sign
        return board
    # for diagonal 2
    elif board[2] == board[4] and isinstance (board[6],int):
        board[6] = comp_sign
        return board
    elif board[4] == board[6] and isinstance (board[2],int):
        board[2] = comp_sign
        return board
    elif board[6] == board[2] and isinstance (board[4],int):
        board[4] = comp_sign
        return board
    
    # for the fork I gave it and this stupid idiot succumbed to that
    global fork
    if board[0] == board[8] and board[4] == comp_sign and fork == 0:
        for i in sides:
            try:
                int(board[i])
                board[i] = comp_sign
                fork = 1
                return board
            except:
                continue
    if board[2] == board[6] and board[4] == comp_sign and fork == 0:
        for i in sides:
            try:
                int(board[i])
                board[i] = comp_sign
                fork = 1
                return board
            except:
                continue
    
    if isinstance(board[4], int):
        board[4] = comp_sign
        return board
    
    corners = [0, 2, 6, 8]
    for corner in corners:
        if isinstance(board[corner], int):
            board[corner] = comp_sign
            return board
            
    for side in sides:
        if isinstance(board[side], int):
            board[side] = comp_sign
            return board

def name_symb_toss():    # takes the name and symbol from player. returns name, signs for player and computer, and whose turn is 1st
    while True:
        p = input("Enter your name: ")    #Takes name
        if p != "" and p != " " and p != "  ":
            break
        else:
            print("C'mon! Don't be boring.", end=" ")
    while True:    #Takes symbol from player
        p_sign = input("Choose your symbol [X] or [O]: ").upper()
        if p_sign != "X" and p_sign!= "O":
            print("Invalid symbol")
        else:
            break
    if p_sign == "X" or p_sign == "x":
        c_sign = "O"
    else:
        c_sign = "X"
    # initiates the toss
    while True:    
        call = input(f"{p}, choose Heads[H] or Tails[T]: ").upper()
        if call == "H":
            call = 1
            break
        elif call == "T":
            call = 2
            break
        else:
            print("Invalid input!")
    coin = random.randint(1,2)
    print("The coin is tossed.", end=" ")
    if coin == 1:
        time.sleep(1)
        print("And it's Heads.", end=" ")
    elif coin == 2:
        time.sleep(1)
        print("And it's Tails.", end=" ")
    if coin == call:
        go_first = p
        print(f"{p} won the toss.")
    else:
        go_first = "arb"
        print("Computer won the toss.")
    return p, p_sign, c_sign, go_first

def player_move(board, player, player_sign):  
    move = int(input("Make your move: "))
    try:    # prevents user inputting a value that's not a number
        int(move)
    except:
        print("That's not in the board :')")
    while move not in board:
        print("Invalid move!")     
        move = int(input("Make your move: "))
    board[move] = player_sign
    return board
fork = 0   # Long story short, it basically helps prevents the infamous 'FORK', which wass the last way to beat it
def main():
    print("Welcome to Tic Tac Toe, if you beat this game, you are entitled to a $1 from FM17!")
    while True:
        board = [0, 1, 2, 3, 4, 5, 6, 7, 8]      # using a list instead of variables since it's easier to pass into fucntions
        player, player_sign, comp_sign, go_1, = name_symb_toss()
        if go_1 == player:
            turn = 1
            print_board(board)
        else:
            turn = 0
        while True:    
            if turn%2 == 1:
                board = player_move(board, player, player_sign)
                turn += 1
                print_board(board)
                if is_winner(board, player_sign) == True:
                    print(f"Congratulation! {player} won the game.")
                    break
                if is_draw(board) == True:
                    print("It's a Draw")
                    break
            elif turn%2 == 0:
                print("Computer is thinking...")
                time.sleep(1)
                board = computer_move(board, comp_sign)
                turn += 1
                print_board(board)
                if is_winner(board, comp_sign) == True:
                    print("You LOST!")
                    break
                if is_draw(board) == True:
                    print("It's a Draw")
                    break            
        print("Do you wanna olay again? (Y/N)")
        play_again = input("")
        if play_again != "Y" and play_again != "y":
            break

main()
