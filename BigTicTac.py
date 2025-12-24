import Labels

BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def new_board():
    board = []
    for x in range(0, BOARD_WIDTH):
        column = []
        for y in range(0, BOARD_HEIGHT):
            column.append(None)
        board.append(column)
    return board

def quit():
    print("Thanks for playing!")
    exit()


def is_board_full(board):
    empty_symbol = None
    is_empty_slot = any(empty_symbol in row for row in board)
    return not is_empty_slot


def render(board):
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)
    row_num = 0
    print("  0 1 2")
    print("  ------")
    for row in rows:
        output_row = '' 
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += str(sq)
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print("  ------")


def get_move():
    position = []
    while True:
        try:
         x = int(input("Enter X coordinate (0-2): "))
        except ValueError:
            print(Labels.INVALID_INPUT_MESSAGE)
            continue
        try:
            y = int(input("Enter Y coordinate (0-2): "))
        except ValueError:
            print(Labels.INVALID_INPUT_MESSAGE)
            continue
        if x == 7 or y == 7:
            quit()
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
        raise Exception("Invalid move: ")
    board[position[0]][position[1]] = player


def get_all_lines():
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

    diagonals = [[[0, 0], [1, 1], [2, 2]],
                 [[0, 2], [1, 1], [2, 0]]]
    return cols + rows + diagonals


def get_winner(board):
    all_lines = get_all_lines()
    for line in all_lines:
        line_values = [board[x][y] for [x, y] in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]
    return None
    

def main_menu():
    print("Welcome to Tic Tac Toe!")
    print("To Start Playing, type 'play'")
    print("To Quit, type 'quit'")
    order = input("Enter your choice: ").strip().lower()
    if order == 'play':
        play()
    elif order == 'quit':
        quit()
    else:
        print(Labels.INVALID_INPUT_MESSAGE)
        main_menu()


def play():
    players = ['X','O']
    board = new_board()
    turn = 0

    print("The board below is in the form of a 3x3 grid."
          "Both rows and columns are numbered 0 to 2."
          "Look carefully which box you want to enter your character and enter its x and y coords."
           "To surrender, type the number 7")

    while True:
        current_player = players[turn % 2]
        print(' ')
        print(f"Player {current_player}'s turn")
        render(board)

        try:
            move_coords = get_move()
            if not is_valid_move(board, move_coords):
                print("Invalid move, try again.")
                continue
        except Exception:  
            print(Labels.INVALID_INPUT_MESSAGE)
        

        make_move(board, move_coords, current_player)

        winner = get_winner(board)
        if winner:
            render(board)
            print(f"The winner is {winner}")
            break

        if (is_board_full(board)):
            print("It's a tie!")
            break

        turn += 1

    
main_menu()   