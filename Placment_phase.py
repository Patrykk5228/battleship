from random import randint
import sys

board = []
player = input("Podaj nick")
is_ai = False
already_chosen = []


def get_board():

    board = []

    for x in range(5):
        board.append(["O"] * 5)

    for row in board:
        print((" ").join(row))
    return board

print("Let's play Battleship!\n")
get_board() # only for check

def display_board(board):

    board = get_board()

    row_list = ("A", "B", "C", "D", "E")
    index = 0
    for row in board:
        if index < 1:
            print('   ' + "1" + '   ' + "2 " + '  ' + "3" + '   ' + "4" + '   ' + "5\n")
        print(row_list[index] + ' ' + ' ' + row[0] + '   ' + row[1] + '   ' + row[2] + '   ' + row[3] + '   ' + row[4])
        index += 1
        print('  '+(''*(len(board)-2))+'')

def player_turn(player):
    round = 0
    if player == 1:
        round += 1
    return round
    pass 

def is_correct_letter(userInput):
    entered_letter = userInput[0].upper()
    if entered_letter.isalpha() == False:
        return False
    return True
 
def is_number(userInput):
    try:
        int(userInput)
    except ValueError:
        return False
    return True

def check_coordinates(player, is_ai, already_chosen):

    round = player_turn(player)
    error_msg = "Invalid input"
    while True:
        
        if round % 2 == 0 or is_ai:
            user_input = input('Player 1 please enter coordinates: ')
        else:
            user_input = input('Player 2 please enter coordinates: ')
        if len(user_input) != 2:
            if user_input == "3":
                print("Bye Bye")
                sys.exit()
            else:
                print(error_msg)
                continue
        isLetter = is_correct_letter(user_input[0])
        isNumber = is_number(user_input[1])
        try:
            coordinate = (user_input[0].upper(), int(user_input[1]))
            if isLetter is False or isNumber is False:
                print(error_msg)
                continue
        except:
            print(error_msg)
            continue
        if coordinate not in already_chosen:
            already_chosen.append(coordinate)
        else:
            print("This coordinate is already occupied!")
            continue
        return coordinate

check_coordinates(player, is_ai, already_chosen)


        
display_board(board) # only for check