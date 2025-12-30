import Labels

BOARD_HEIGHT = 20
BOARD_WIDTH = 20
WIN_CONDITION = 4
# good use of const

# why create new file, why not use branching (deleting the file )
# Github can track delete operations


def new_board():
    board = []
    for x in range(0, BOARD_WIDTH):
        column = []
        for y in range(0, BOARD_HEIGHT):
            column.append(None)
        board.append(column)
    return board


def exit_game():
    print("Thanks for playing!") # why not use labels
    exit()




def is_board_full(board):
    empty_symbol = None
    is_empty_slot = any(empty_symbol in row for row in board)
    return not is_empty_slot


def render(board): # alignment difficult to see, no seperator within grid
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)
    row_num = 0
    header = " "
    for index in range(BOARD_WIDTH):
        header += f" {index}"
    print(header)
    separator = " " + "-" * (BOARD_WIDTH * 2 + 1)
    print(separator)
    for y in range(BOARD_HEIGHT):
        row_cells = []
        for x in range(BOARD_WIDTH):
            cell = board[x][y]
            row_cells.append(" " if cell is None else str(cell))

        print(f"{y}|{' '.join(row_cells)}|")
    print(separator)


def get_move():
    position = []
    while True:
        try:
            x = int(input(f"Enter X coordinate (0-{BOARD_WIDTH - 1}): ")) #can string.format or any equivalent function be used
        except ValueError:
            print(Labels.INVALID_INPUT_MESSAGE)
            continue
        try:
            y = int(input(f"Enter Y coordinate (0-{BOARD_HEIGHT - 1}): ")) #can string.format or any equivalent function be used
        except ValueError:
            print(Labels.INVALID_INPUT_MESSAGE)
            continue
        if x == 7 or y == 7: # hardcoded value, What is '7' ?
            exit_game()
        position.append(x)
        position.append(y)
        return position


def is_valid_move(board, position):
    if position[0] < 0 or position[0] >= BOARD_WIDTH:
        return False
    if position[1] < 0 or position[1] >= BOARD_HEIGHT:
        return False
    if board[position[0]][position[1]] is not None:
        return False
    return True


def make_move(board, position, player):
    if not is_valid_move(board, position):
        raise Exception("Invalid move: ") # why not use labels ?
    board[position[0]][position[1]] = player


def get_all_lines(): #can be further broken down in different methonds
    cols = []
    for x in range(0, BOARD_WIDTH):
        col = []
        for y in range(0, BOARD_HEIGHT):
            col.append([x, y])
        cols.append(col)

    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append([x, y])
        rows.append(row)
    #diagonal works
    #diagonal works

    diagonals1 = [] #Difference between diagonal1 vs diagonal2
    for x in range(0, BOARD_WIDTH):
        for y in range(0, BOARD_HEIGHT):
            diag1 = []
            for step in range(0, WIN_CONDITION):
                col = x + step
                row = y + step
                if col >= BOARD_WIDTH or row >= BOARD_HEIGHT:
                    break
                diag1.append([col, row])
            if len(diag1) == WIN_CONDITION: #alternate variable name for diag1 eg. currentLine
                diagonals1.append(diag1)

    diagonals2 = []
    for x in range(0, BOARD_WIDTH):
        for y in range(0, BOARD_HEIGHT):
            diag2 = []
            for step in range(0, WIN_CONDITION):
                col = x - step
                row = y + step
                if col < 0 or row >= BOARD_HEIGHT:
                    break
                diag2.append([col, row])
            if len(diag2) == WIN_CONDITION:
                diagonals2.append(diag2)

    return cols + rows + diagonals1 + diagonals2


def get_winner(board):
    all_lines = get_all_lines()
    for line in all_lines:
        line_values = [board[x][y] for [x, y] in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]
    return None


def main_menu():
    print("        Welcome to Tic Tac Toe!") ## use Labels, hardcoded strings
    print("To Start Playing,         type 'play'")
    print("To Quit,                  type 'quit'")
    order = input("Enter your choice: ").strip().lower()
    if order == "play": # is a switch/case better
        play()
    elif order == "quit":
        exit_game()
    else:
        print(Labels.INVALID_INPUT_MESSAGE)
        main_menu()


def play():
    players = ["X", "O"] ## hardcoded values
    board = new_board()
    turn = 0

    print(f"The board below is in the form of a {BOARD_WIDTH}x{BOARD_HEIGHT} grid.") ## labels plus string format
    print(f"Both rows and columns are numbered 0 to {BOARD_HEIGHT - 1}.")
    print(
        "Look carefully which box you want to enter your character and enter its x and y coords."
    )
    print("To surrender, type the number 7") ## what is number 7 ?, why not surrender ?

    # have to type '7' 2 times for surrender
    # 5 in a row does not win the game

    while True:
        current_player = players[turn % 2]
        print(" ")
        print(f"Player {current_player}'s turn") ## labels plus string.format
        render(board)

        try:
            move_coords = get_move()
            if not is_valid_move(board, move_coords):
                print("Invalid move, try again.")
                continue
        except Exception:
            print(Labels.INVALID_INPUT_MESSAGE)

        #does not show current player when playing clearly

        make_move(board, move_coords, current_player)

        winner = get_winner(board)
        if winner:
            render(board)
            print(f"The winner is {winner}!!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break
#when player wins, no way to play again 
#play again, quit option
        turn += 1


main_menu()


#different files not used 
#main file should only include one function
#labels not properly used 
#zombie code (TicTac.py) present 
# no branch used for new changes 
# new code changes, should be done on a branch, then merged to master
# similar to this change, done on a branch to be merged on master


## Please check if all methods only do one job, if a method does more than one job, please break it down
## Try clearing out terminal when game is in session