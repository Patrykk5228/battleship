import sys

coordinates = [[]]

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

def check_coordinates(board, already_chosen, is_ai):
    error_msg = "Enter correct coordinates."
    round = player_turn()
    while True:
        
        if round % 2 == 0 or is_ai:
            user_input = input('Player 1 please enter coordinates: ')
        else:
            user_input = input('Player 2 please enter coordinates: ')
        if len(user_input) != 2:
            if user_input == "quit":
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
    pass

def get_player_coordinates():
    pass

def get_game_status():
    pass

def player_turn(player):
    round = 0
    if player == 1:
        round += 1
    return round
    pass 
