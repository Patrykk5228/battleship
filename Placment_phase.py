from random import randint

board = []

def print_board(board):

    for x in range(5):
        board.append(["O"] * 5)

    for row in board:
        print((" ").join(row))

print("Let's play Battleship!")
print_board(board)