game = [[1, 1, 1],
        [1, 0, 0],
        [0, 1, 1]]


def game_board(game_map, player=0, row=0, column=0):

    try:
        print("   0  1  2")
        game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
    except IndexError as e:
        print("Something went wrong! Make sure you input row/column as 0 1 or 2?", e)
    finally:
        print("The program is done running")


def win(current_game):
    win = False
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Winner")
            break


# game_board(game_map=game, player=1, row=1, column=1)
win(current_game=game)
