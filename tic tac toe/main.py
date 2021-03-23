import itertools


def game_board(game_map, player=0, row=0, column=0, just_display=False):

    if just_display == True:
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate((game_map)):
            print(count, row)
    else:
        try:
            if game_map[row][column] != 0:
                print('This position is ocupated!')
                return game_map, False
            game_map[row][column] = player
            print("   0  1  2")
            for count, row in enumerate((game_map)):
                print(count, row)
            return game_map, True
        except IndexError as e:
            print("Something went wrong! Make sure you input row/column as 0 1 or 2?", e)
            return game_map, False


def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    else:
        return False


# Function which detects a horizontal winner
def horizontal_win(current_game):
    for row in current_game:
        if all_same(row):
            print("Winner horizontal")
            return True

# Function which detects vertical winner


def vertical_win(current_game):
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print("Winner vertical")
            return True


# Function which detects diagonal winner
def diagonal_win(current_game):
    diags_rev = []
    diags = []
    rows = range(len(current_game))
    cols = reversed(range(len(current_game)))
    for row, col in zip(rows, cols):
        diags_rev.append(current_game[row][col])
        diags.append(current_game[row][row])
    if all_same(diags):
        print('Winner diagonal (/)')
        return True
    elif all_same(diags_rev):
        print('Winner diagonal (\\)')
        return True


def win(current_game):
    if diagonal_win(current_game):
        return True
    elif vertical_win(current_game):
        return True
    elif horizontal_win(current_game):
        return True
    else:
        return False


play = True
players = [1, 2]
while play:
    game_size = 3
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game_board(game, just_display=True)
    player_choice = itertools.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(
                input("What column do you want to play? (0,1,2) : "))
            row_choice = int(input("What row do you want to play? (0,1,2) : "))
            game, played = game_board(
                game, current_player, row_choice, column_choice)
            if win(game):
                game_won = True
                again = input(
                    "The game is over, would you like to play again? (y/n)")
                if again.lower() == 'y':
                    print("Restarting")
                elif again.lower() == 'n':
                    print("Bye bye!")
                    play = False
                else:
                    print("Invalid answer, c u l8r mmgvo")
                    play = False
