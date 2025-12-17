
board_height = 3
board_width = 3


def new_board():
    board = []
    for x in range(0, board_width):
        column = []
        for y in range(0, board_height):
            column.append(None)
        board.append(column)
    return board


def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is None:
                return False
    return True


def render(board):
    rows = []
    for y in range(0, board_height):
        row = []
        for x in range(0, board_width):
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
    x = int(input("Enter X coordinate (0-2): "))
    position.append(x)
    y = int(input("Enter Y coordinate (0-2): "))
    position.append(y)
    return position


def is_valid_move(board, position):
    if position[0] >= board_width:
        
        return False
    if position[1] < 0 or position[1] >= board_height:
        return False
    if board[position[0]][position[1]] is not None:
        return False
    return True



def make_move(board, position, player):
    if is_valid_move(board, position) == False:
        raise Exception("Invalid move: ")
    board[position[0]][position[1]] = player


def get_all_lines():
    cols = []
    for x in range(0, board_width):
        col = []
        for y in range(0, board_height):
            col.append([x, y])
        cols.append(col)

    rows = []
    for y in range(0, board_height):
        row = []
        for x in range(0, board_width):
            row.append([x, y])
        rows.append(row)

    diagonals = [
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    return cols + rows+ diagonals


def get_winner(board):
    all_lines = get_all_lines()
    for line in all_lines:
       line_values = [board[x][y] for [x,y] in line]
       if len(set(line_values)) == 1 and line_values[0] is not None:
              return line_values[0]
    return None
    

def play(player1_f, player2_f):
    players = [
        ('X', player1_f),
        ('O', player2_f)
    ]

    turn = 0
    board = new_board()
    while True:
        current_player_id, current_player_f = players[turn % 2]
        render(board)

        move_coords = get_move()
        make_move(current_player_id, board, move_coords)

        winner = get_winner(board) 
        if winner is not None:
            render(board)
            print(f'The winner is {winner}!')
            break

        if is_board_full(board):
            render(board)
            print("It's a draw!")
            break

        turn += 1

play('player1_f', 'player2_f')



