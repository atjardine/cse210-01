'''Tic-tac-toe game
Author: Alysha Jardine'''

def main():

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("----")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw_game(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True