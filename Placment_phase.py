from random import randint

board = []

def print_board(board):

    for x in range(5):
        board.append(["O"] * 5)

    for row in board:
        print((" ").join(row))

print("Let's play Battleship!\n")
print_board(board)

def display_board():

    row_list = ("A", "B", "C", "D", "E")
    index = 0
    for row in board:
        if index < 1:
            print('   ' + "1" + '   ' + "2 " + '  ' + "3" + '   ' + "4" + '   ' + "5\n")
        print(row_list[index] + ' ' + ' ' + row[0] + '   ' + row[1] + '   ' + row[2] + '   ' + row[3] + '   ' + row[4])
        index += 1
        print('  '+(''*(len(board)-2))+'')
display_board()