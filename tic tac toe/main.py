game = [[0, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]


def game_board(game_map, player=0, row=0, column=0):

    try:
        print("   0  1  2")
        game_map[row][column] = player
        for count, row in enumerate(reversed(game_map)):
            print(count, row)
    except IndexError as e:
        print("Something went wrong! Make sure you input row/column as 0 1 or 2?", e)
    finally:
        print("The program is done running")


"""
def win(current_game):
    win = False
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Winner")
            break
"""


def diagonal_win(current_game):
    diags_rev = []
    diags = []
    rows = range(len(current_game))
    cols = reversed(range(len(current_game)))
    for row, col in zip(rows, cols):
        print(row, col)
        diags_rev.append(current_game[row][col])
        diags.append(current_game[row][row])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print('Winner')
    elif diags_rev.count(diags_rev[0]) == len(diags_rev) and diags_rev[0] != 0:
        print('Winner')


diagonal_win(game)
