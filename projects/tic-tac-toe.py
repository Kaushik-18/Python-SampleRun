# better way is to create a 2D array , so that we can play for any size
game_board = [' '] * 10
game_state = True


def display_board(game_board):
    print(" " + game_board[7] + " | " + game_board[8] + " | " + game_board[9])
    print("----------")
    print(" " + game_board[4] + " | " + game_board[5] + " | " + game_board[6])
    print("----------")
    print(" " + game_board[1] + " | " + game_board[2] + " | " + game_board[3])
    print("----------")


def check_valid_position(board, positon):
    if board[positon] == ' ':
        return True
    else:
        return False


def get_user_input(game_board):
    while True:
        try:
            position = int(input())
            if position not in range(1, 10):
                print("Input number between 1 - 9")
                continue
        except ValueError:
            print("Input number between 1 - 9")
            continue

        if not check_valid_position(game_board, position):
            print("Position already full !")
        else:
         return position


def create_marker(marker, game_board, position):
    game_board[position] = marker


def check_win(board, marker):
    if board[1] == board[2] == board[3] == marker or \
                                    board[1] == board[4] == board[7] == marker or \
                                    board[2] == board[5] == board[8] == marker or \
                                    board[3] == board[6] == board[9] == marker or \
                                    board[1] == board[5] == board[9] == marker or \
                                    board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


def check_board_full():
    if " " in game_board[1:]:
        return False
    return True


def get_player_choice(marker, game_board):
    print('Select your position ')
    position = get_user_input(game_board)
    create_marker(marker, game_board, position)
    display_board(game_board)
    if check_win(game_board, marker):
        return False, marker + " wins !"
    elif check_board_full():
        return False, "Its a tie !"
    else:
        return True, ""


def play_game():
    X = 'x'
    O = 'o'
    global game_board, game_state
    game_board = [' '] * 10
    game_state = True

    while game_state:
        # PLAYER CHOICE FOR MARKER X
        print("Player 1")
        game_state, statement = get_player_choice(X, game_board)
        print(statement)
        if not game_state:
            return
        print('Player 2')
        game_state, statement = get_player_choice(O, game_board)
        print(statement)
        if not game_state:
            return

    query = input("Do you wish to continue? Y/N")
    if query == 'Y':
        play_game()
    else:
        print("Game Ends !")


print("Welcome to the game !")
play_game()
