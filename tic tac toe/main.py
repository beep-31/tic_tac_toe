game =  [[0,0,0],
         [0,0,0],
         [0,0,0]]

def game_board():
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)

game_board()

game[0][1] = 1

game_board()