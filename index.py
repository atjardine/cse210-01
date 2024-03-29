'''Tic-tac-toe game
Author: Alysha Jardine'''

def main():
    player = next_player("")
    board = create_board()
    while not (winner(board) or draw_game(board)):
        display_board(board)
        turn(player, board)
        player = next_player(player)
    display_board(board)
    print(f"Good game. Thanks for playing, come back soon for a rematch!")
    
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw_game(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[0] == board[3] == board[6] or
            board[0] == board[4] == board[8] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[2] == board[4] == board[6] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8])

def turn(player, board):
    square = int(input(f"{player}'s turn to play, select square (1-9): "))
    board[square - 1] = player

def next_player(now):
    if now == "" or now == "o":
        return "x"
    if now == "" or now == "x":
        return "o"

if __name__ =="__main__":
    main()